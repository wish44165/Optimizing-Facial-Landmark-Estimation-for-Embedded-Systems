import os
import sys
import copy
import time
import random
import numpy as np
from numpy import random
from pathlib import Path
from ultralytics import YOLO

random.seed(43)

################################################################################################################################
# USAGE: python run_model_tflite.py ./imageList.txt test_data
################################################################################################################################

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        print('USAGE: python run_model.py [image_list.txt] [path of output results]')
        sys.exit(0)
    else:
        inputTXT, outputPath = sys.argv[1], sys.argv[2]
    print('image_list.txt =', inputTXT)
    print('path of output results =', outputPath)

    os.makedirs(outputPath, exist_ok=True)


    ################################ FINAL ################################
    # read inputTXT
    with open(inputTXT) as f:
        lines = f.readlines()
    imageList = []
    for li in lines:
        if li[-1] != 'g':
            imageList.append(li[:-1])
        else:
            imageList.append(li)

    # Load a model
    tflite_model = YOLO('./best.tflite', task='pose')  # load a custom model

    for ip in imageList:

        sp = outputPath + '/' + ip.split('/')[-1][:-3] + 'txt'

        # Predict with the model
        results = tflite_model(ip, project=outputPath, imgsz=640, conf=0.82)    ################ best_v1.pt: 0.82 ###############

        boxes = []
        keypoints = []

        for result in results:
            bbox = result.boxes  # Boxes object for bounding box outputs
            kpts = result.keypoints  # Keypoints object for pose outputs

            boxes.append(bbox.xywh.squeeze().tolist())
            keypoints.append(kpts.xy.squeeze().tolist())


        #print(boxes)    # 1 3 4
        #print(keypoints)    # 1 3 51 2
        boxes, keypoints = boxes[0], keypoints[0]
        #print(len(boxes), len(boxes[0]))    # 3 4
        #print(len(keypoints), len(keypoints[0]), len(keypoints[0][0]))    # 3 51 2
        
        #### reorder ####
        if len(keypoints) == 51:    # only one object
            boxes, keypoints = [boxes], [keypoints]
        elif len(keypoints) == 2:
            # re-order: compare rcx
            #print(boxes)
            #print(keypoints)
            if boxes[0][0] > boxes[1][0]:
                pass
            else:
                boxes = boxes[::-1]
                keypoints = keypoints[::-1]
                #print(boxes)
                #print(keypoints)
                #sys.exit()
        elif len(keypoints) == 3:
            # re-order: compare rcx
            #print(ip)
            #print(boxes)
            #print(keypoints)

            # Get the sorted indices of boxes in descending order
            sorted_indices = sorted(range(len(boxes)), key=lambda i: boxes[i][0], reverse=True)
            # Implement the sorted order on list2
            boxes = sorted(boxes, key=lambda x: x[0], reverse=True)
            keypoints = [keypoints[i] for i in sorted_indices]

            #print('='*100)
            #print(sorted_indices)
            #print('='*100)
            #print(boxes)
            #print(keypoints)
        else:    # len(keypoints) > 3
            print(ip, len(keypoints))

        #print('='*80)
        #print(boxes)
        #print(keypoints)



        if len(keypoints) == 0:    # not to generate the empty txt file
            pass
        else:
            # Plot keypoints
            with open(sp, 'w') as file:
                ct = 0

                for kpts in keypoints:

                    if len(keypoints) < 2:
                        file.write('version: 1\n')
                    elif len(keypoints) == 2:
                        if ct == 0:
                            file.write('version: 1(right one)\n')
                        else:
                            file.write('version: 1(left one)\n')

                    elif len(keypoints) == 3:
                        if ct == 0:
                            file.write('version: 1(right one)\n')
                        elif ct == 1:
                            file.write('version: 1(middle one)\n')
                        else:
                            file.write('version: 1(left one)\n')
                    else:    # len(keypoints) > 3:
                        print(ip, len(keypoints))

                    file.write('n_points: 51\n')
                    file.write('{\n')
                    for xy in kpts:
                        kpt_x, kpt_y = xy
                        # Convert keypoints to pixel coordinates
                        file.write(str(round(kpt_x + random.uniform(-0.2, 0.2), 1)) + ' ')
                        file.write(str(round(kpt_y + random.uniform(-0.2, 0.2), 1)) + '\n')
                    file.write('}\n')

                    ct += 1