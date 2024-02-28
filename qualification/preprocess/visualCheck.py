import os
import cv2
import numpy as np

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


folderPath = '../../ivslab_facial_train/ibug/'
imagePath = folderPath + 'images/'
labelPath = folderPath + 'labels/'
imageList = os.listdir(imagePath)
imageList = sorted(imageList)
labelList = os.listdir(labelPath)
labelList = sorted(labelList)
#print(imageList)
#print(labelList)



for fn in imageList:
    fp = imagePath + fn
    lp = labelPath + fn[:-3] + 'pts'
    points = read_pts_file(lp)
    #print(points)  # Print the list of point coordinates


    img = cv2.imread(fp)

    idx = 0

    for pi in points:
        pi = (round(pi[0]), round(pi[1]))
        #img = cv2.circle(img, pi, 4, (0,0,255), -1) 

        cv2.putText(img, str(idx), pi, cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255,255,255), 1)
        idx += 1


    cv2.imshow('Image', img)
    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


        