import os
import cv2

def read_pts_file(file_path, width, height):

    # read file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # bounding box info
    points = [0, 0.5, 0.5, 1, 1]    # classid, rcx, rcy, rw, rh

    # convert pts to yolo txt format
    start_index = lines.index('{\n') + 1
    for line in lines[start_index:]:
        if line == '}\n' or line == '}':
            break
        x, y = map(float, line.split())
        x /= width
        y /= height
        x = "{:.6f}".format(x)
        y = "{:.6f}".format(y)
        points.append(x)
        points.append(y)
        points.append("2.000000")

    return points

datafolderPath = '/home/wish/UoM/0thers/IEEE_ICME_2024_Grand_Challenges/src/preprocess/data/'

datasets = ['train', 'val']

for dataType in datasets:

    imagePath = datafolderPath + 'images/' + dataType + '/'
    imageList = os.listdir(imagePath)
    imageList = sorted(imageList)
    labelPath = datafolderPath + 'labels/' + dataType + '/'
    labelList = os.listdir(labelPath)
    labelList = sorted(labelList)

    #os.makedirs(outputPath, exist_ok=True)

    for imn in imageList:
        imp = imagePath + imn
        
        ln = imn[:-3] + 'pts'
        lp = labelPath + ln

        img = cv2.imread(imp)
        h, w = img.shape[:2]

        #print(read_pts_file(lp, w, h))
        #print(len(read_pts_file(lp, w, h)))

        # Specify the file path
        op = labelPath + imn[:-3] + 'txt'

        # write file
        with open(op, 'w') as f:
            # Iterate through the list and write each element to a new line in the file
            for di in read_pts_file(lp, w, h):
                f.write(str(di) + ' ')