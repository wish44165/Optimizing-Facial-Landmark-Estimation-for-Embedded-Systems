import os
import cv2
import numpy as np


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

folderPath = '../../datasets/ivslab_facial_train_filtered/300W/'
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
    lp = labelPath + fn[:-3] + 'txt'

    with open(lp, 'r') as file:
        data = file.readlines()
        # Parse the data
        boxes, keypoints = parse_data(data)
        #print(boxes, keypoints)

        """
        # Plot the image and overlay bounding boxes and keypoints
        image = plt.imread(fp)
        plt.imshow(image)

        height, width, _ = image.shape


        # Plot bounding boxes
        for obj_class, box in boxes:
            x, y, w, h = box
            # Convert (x, y, w, h) to (xmin, ymin, xmax, ymax)
            xmin = x - w / 2
            ymin = y - h / 2
            xmax = x + w / 2
            ymax = y + h / 2
            plt.gca().add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor='r', facecolor='none'))
            plt.text(xmin, ymin, f'Class {obj_class}', color='r')

        # Plot keypoints
        for kpts in keypoints:
            for i in range(0, len(kpts), 3):
                x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                if visibility > 0:  # Only plot visible keypoints
                    plt.scatter(x*width, y*height, color='g', s=10)

        plt.axis('off')
        plt.show()
        """

        # Read the image
        image = cv2.imread(fp)

        # Get the height and width of the image
        height, width, _ = image.shape

        # Plot bounding boxes
        for obj_class, box in boxes:
            x, y, w, h = box
            # Convert (x, y, w, h) to pixel coordinates
            xmin = int((x - w / 2) * width)
            ymin = int((y - h / 2) * height)
            xmax = int((x + w / 2) * width)
            ymax = int((y + h / 2) * height)
            # Draw bounding box rectangle
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
            cv2.putText(image, f'Class {obj_class}', (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        # Plot keypoints
        for kpts in keypoints:
            for i in range(0, len(kpts), 3):
                x, y, visibility = kpts[i], kpts[i+1], kpts[i+2]
                if visibility > 0:  # Only plot visible keypoints
                    # Convert keypoints to pixel coordinates
                    kpt_x = int(x * width)
                    kpt_y = int(y * height)
                    # Draw keypoints
                    cv2.circle(image, (kpt_x, kpt_y), 3, (0, 255, 0), -1)

        # Display the image
        cv2.imshow('Image with Bounding Boxes and Keypoints', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        """
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
        """
        
