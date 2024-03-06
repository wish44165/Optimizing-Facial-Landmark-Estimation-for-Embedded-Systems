import os
import cv2
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

predictPath = '/home/wish/pro/ICME2024/src/ultralytics/runs/facial/predict2/labels/'
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
    
    # Plot keypoints
    with open(sp, 'w') as file:
        ct = 0
        for kpts in keypoints:
            if len(keypoints) > 1:

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

                if ct == 0:
                    file.write('version: 1(Right)\n')
                else:
                    file.write('version: 1(Left)\n')
            else:
                file.write('version: 1\n')
            file.write('n_points: 51\n')
            file.write('{\n')
            for i in range(0, len(kpts), 3):
                x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                if visibility > 0:  # Only plot visible keypoints
                    # Convert keypoints to pixel coordinates
                    kpt_x, kpt_y = x * width, y * height
                    file.write(str(kpt_x) + ' ')
                    file.write(str(kpt_y) + '\n')
            file.write('}\n')

            ct += 1


print(checkList)