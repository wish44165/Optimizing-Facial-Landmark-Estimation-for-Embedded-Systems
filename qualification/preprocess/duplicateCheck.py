import os
import cv2
import shutil
import numpy as np
import matplotlib.pyplot as plt

def read_pts_file(filename):
    points = []

    with open(filename, 'r') as f:
        # Read the header information
        version = f.readline().strip().split(': ')[1]
        n_points = int(f.readline().strip().split(': ')[1])

        # Skip the opening bracket
        f.readline()

        # Read each line and extract point coordinates
        for _ in range(n_points):
            line = f.readline().strip()
            if line == '}':
                break
            # Remove leading/trailing whitespace and split the line into coordinates
            parts = line.split()
            # Convert coordinates to floats
            x, y = map(float, parts)
            # Append the point coordinates to the list
            points.append((x, y))

    return points

# original data path
datafolderPath = '../../datasets/ivslab_facial_train/'
datafolderList = os.listdir(datafolderPath)
datafolderList = sorted(datafolderList)

# labeled yolo format path
labeledPath = '../../datasets/yolo_labels/'

# new data path
filteredPath = '../../datasets/ivslab_facial_train_filtered/'
os.makedirs(filteredPath, exist_ok=True)

# save duplicate result folder
duplicateimagePath = '../../datasets/ivslab_facial_train_filtered_details/'
os.makedirs(duplicateimagePath, exist_ok=True)

for foldern in datafolderList:

    print('-' * 20, foldern, '-' * 20)

    folderPath = datafolderPath + foldern + '/'
    imagePath = folderPath + 'images/'
    labelPath = folderPath + 'labels/'
    imageList = os.listdir(imagePath)
    imageList = sorted(imageList)
    labelList = os.listdir(labelPath)
    labelList = sorted(labelList)
    #print(len(imageList))
    #print(len(labelList))


    duplicateDict = dict()

    for fn in imageList:

    # debug
    #for i in range(100):
    #    fn = imageList[i]

        fp = imagePath + fn
        lp = labelPath + fn[:-3] + 'pts'

        img = cv2.imread(fp)

        if str(np.sum(img)) not in set(duplicateDict.keys()):
            duplicateDict[str(np.sum(img))] = [fn]
        else:
            duplicateDict[str(np.sum(img))].append(fn)

    max_length_key = max(duplicateDict, key=lambda k: len(duplicateDict[k]))
    #print(duplicateDict)
    #print(max_length_key)
    #print(len(duplicateDict[max_length_key]))

    # plot width
    ni = int(np.sqrt(len(duplicateDict[max_length_key]))) + 1


    # labeled yolo format txt
    labeledfolderPath = labeledPath + foldern + '_labels/'
    labeledfolderList = os.listdir(labeledfolderPath)
    labeledfolderList = sorted(labeledfolderList)
    #print(labeledfolderList)


    # new data structure
    filteredfolderPath = filteredPath + foldern + '/'
    os.makedirs(filteredfolderPath, exist_ok=True)
    filteredfolderPath_image = filteredfolderPath + 'images/'
    filteredfolderPath_labels = filteredfolderPath + 'labels/'
    os.makedirs(filteredfolderPath_image, exist_ok=True)
    os.makedirs(filteredfolderPath_labels, exist_ok=True)


    # filter procedure
    for key, value in duplicateDict.items():

        if len(value) > 1:

            # visualize
            ct = 1
            plt.figure()
            for fi in value:
                if ct == 1:
                    outImageN = fi
                plt.subplot(ni, ni, ct)
                fp = imagePath + fi
                img = cv2.imread(fp)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                plt.imshow(img)
                plt.title(fi)
                plt.axis('off')
                ct += 1
            #plt.show()
            plt.tight_layout()
            plt.savefig(duplicateimagePath + foldern + '_' + outImageN)
            plt.close()
            

            # combine txt file
            idx = 1
            infoList = []
            for fi in value:
                fp = imagePath + fi
                lp = labeledfolderPath + fi[:-3] + 'txt'
                
                # copy image
                if idx == 1:
                    shutil.copyfile(fp, filteredfolderPath_image + fi)

                    outputN = fi[:-3] + 'txt'
                
                # store all info for the same image
                with open(lp, 'r') as rf:
                    lines = rf.readlines()[0]
                    infoList.append(lines)

                idx += 1

            # write new txt file
            with open(filteredfolderPath_labels + outputN, 'w') as wf:
                for info in infoList:
                    wf.write(info + '\n')

        else:
            fi = value[0]
            fp = imagePath + fi
            lp = labeledfolderPath + fi[:-3] + 'txt'

            # copy image and txt
            shutil.copyfile(fp, filteredfolderPath_image + fi)
            shutil.copyfile(lp, filteredfolderPath_labels + fi[:-3] + 'txt')