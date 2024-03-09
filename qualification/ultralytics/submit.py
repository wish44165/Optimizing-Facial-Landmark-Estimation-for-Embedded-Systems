import os
import cv2
import sys
import copy

# Function to parse the data and extract bounding box coordinates
def parse_data(data):
    boxes = []
    keypoints = []
    for line in data:
        line = line.strip().split()
        # Extract object class (assuming it's the first value)
        obj_class = int(line[0])
        # Extract bounding box coordinates
        box = [float(coord) for coord in line[1:5]]
        boxes.append((obj_class, box))
        # Extract keypoints
        keypoints.append([float(coord) for coord in line[5:]])

    return boxes, keypoints

predictPath = '/home/wish/pro/ICME2024/qualification/ultralytics/runs/facial/predict/labels/'
predictList = os.listdir(predictPath)
predictList = sorted(predictList)
#print(len(predictList))

imagePath = '/home/wish/pro/ICME2024/datasets/ivslab_facial_test_private_qualification/'
imageList = os.listdir(imagePath)
imageList = sorted(imageList)
#print(len(imageList))

checkList = copy.deepcopy(imageList)

savePath = './test_data/'
os.makedirs(savePath, exist_ok=True)

for predictn in predictList:
    pp = predictPath + predictn
    ip = imagePath + predictn[:-3] + 'png'
    sp = savePath + predictn

    checkList.remove(predictn[:-3] + 'png')

    img = cv2.imread(ip)
    height, width = img.shape[:2]
    #print(height, width)

    with open(pp, 'r') as file:
        data = file.readlines()

    boxes, keypoints = parse_data(data)

    #### reorder ####
    if len(keypoints) < 2:
        pass
    elif len(keypoints) == 2:
        # re-order: compare rcx
        #print(boxes)
        #print(keypoints)
        if boxes[0][1][0] > boxes[1][1][0]:
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
        sorted_indices = sorted(range(len(boxes)), key=lambda i: boxes[i][1], reverse=True)
        # Implement the sorted order on list2
        boxes = sorted(boxes, key=lambda x: x[1][0], reverse=True)
        keypoints = [keypoints[i] for i in sorted_indices]

        #print('='*100)
        #print(sorted_indices)
        #print('='*100)
        #print(boxes)
        #print(keypoints)
    else:    # len(keypoints) > 3
        print(ip, len(keypoints))
    
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
            for i in range(0, len(kpts), 3):
                x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                if visibility > 0:  # Only plot visible keypoints
                    # Convert keypoints to pixel coordinates
                    kpt_x, kpt_y = x * width, y * height
                    file.write(str(round(kpt_x, 1)) + ' ')
                    file.write(str(round(kpt_y, 1)) + '\n')
            file.write('}\n')

            ct += 1

print(checkList)