import os
from sklearn.model_selection import train_test_split
import shutil

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

prevLeadPath = '/home/wish/pro/ICME2024/qualification/ultralytics/runs/facial/predict2/labels/'
prevLeadList = os.listdir(prevLeadPath)
prevLeadList = sorted(prevLeadList)

imagePath = '/home/wish/pro/ICME2024/datasets/ivslab_facial_test_private_qualification/'
imageList = os.listdir(imagePath)
imageList = sorted(imageList)

savePath = '/home/wish/pro/ICME2024/datasets/t1/'
os.makedirs(savePath, exist_ok=True)
saveImagePath = savePath + 'images/'
saveLabelPath = savePath + 'labels/'
os.makedirs(saveImagePath, exist_ok=True)
os.makedirs(saveLabelPath, exist_ok=True)
saveImageTrainPath = saveImagePath + 'train/'
saveImageValPath = saveImagePath + 'val/'
saveLabelTrainPath = saveLabelPath + 'train/'
saveLabelValPath = saveLabelPath + 'val/'
os.makedirs(saveImageTrainPath, exist_ok=True)
os.makedirs(saveImageValPath, exist_ok=True)
os.makedirs(saveLabelTrainPath, exist_ok=True)
os.makedirs(saveLabelValPath, exist_ok=True)

image_train, image_val = train_test_split(imageList, test_size=0.2, random_state=42)

for imgn in image_train:
    ip = imagePath + imgn
    lp = prevLeadPath + imgn[:-3] + 'txt'
    sip = saveImageTrainPath + imgn
    slp = saveLabelTrainPath + imgn[:-3] + 'txt'

    try:
        with open(lp, 'r') as file:
            data = file.readlines()
        
        boxes, keypoints = parse_data(data)
        #print(data)
        #print(keypoints)
        
        with open(slp, 'w') as file:

            for i in range(len(keypoints)):
                boxi = boxes[i]
                kpts = keypoints[i]

                stkpts = ''
                for i in range(0, len(kpts), 3):
                    x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                    sti = str(x) + ' ' + str(y) + ' 2 '
                    #print(sti)
                    stkpts += sti
                
                # write txt
                strboxi = str(boxi[1][0]) + ' ' + str(boxi[1][1]) + ' ' + str(boxi[1][2]) + ' ' + str(boxi[1][3])
                file.write('0 ' + strboxi + ' ' + stkpts + '\n')

                # copy image
                shutil.copy(ip, sip)
    except:
        pass

for imgn in image_val:
    ip = imagePath + imgn
    lp = prevLeadPath + imgn[:-3] + 'txt'
    sip = saveImageValPath + imgn
    slp = saveLabelValPath + imgn[:-3] + 'txt'

    try:
        with open(lp, 'r') as file:
            data = file.readlines()
        
        boxes, keypoints = parse_data(data)
        #print(data)
        #print(keypoints)
        
        with open(slp, 'w') as file:

            for i in range(len(keypoints)):
                boxi = boxes[i]
                kpts = keypoints[i]

                stkpts = ''
                for i in range(0, len(kpts), 3):
                    x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                    sti = str(x) + ' ' + str(y) + ' 2 '
                    #print(sti)
                    stkpts += sti
                
                # write txt
                strboxi = str(boxi[1][0]) + ' ' + str(boxi[1][1]) + ' ' + str(boxi[1][2]) + ' ' + str(boxi[1][3])
                file.write('0 ' + strboxi + ' ' + stkpts + '\n')

                # copy image
                shutil.copy(ip, sip)
    except:
        pass