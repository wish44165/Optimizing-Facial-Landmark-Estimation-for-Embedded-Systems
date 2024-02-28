import os
import cv2

relaxPixels = 20

def read_pts_file_o(filename):
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

def read_pts_file(file_path, width, height):

    # read file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # bounding box info
    #points = [0, 0.5, 0.5, 1, 1]    # classid, rcx, rcy, rw, rh

    points = []

    xmin, ymin, xmax, ymax = width, height, 0, 0

    # convert pts to yolo txt format
    start_index = lines.index('{\n') + 1
    for line in lines[start_index:]:
        if line == '}\n' or line == '}':
            break
        x, y = map(float, line.split())

        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y

        x /= width
        y /= height
        x = "{:.6f}".format(x)
        y = "{:.6f}".format(y)
        points.append(x)
        points.append(y)
        points.append("2.000000")
    

    xmin -= relaxPixels
    xmax += relaxPixels
    ymin -= relaxPixels
    ymax += relaxPixels

    if xmin < 1:
        xmin = 1
    if ymin < 1:
        ymin = 1
    if xmax > width:
        xmax = width
    if ymax > height:
        ymax = height
    

    return [0, ((xmax + xmin) / 2) / width, ((ymax + ymin) / 2) / height, (xmax - xmin) / width, (ymax - ymin) / height] + points

datafolderPath = '../../datasets/data_v1/'

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

        # visualize
        """
        ## circle
        points = read_pts_file_o(lp)
        for pi in points:
            pi = (round(pi[0]), round(pi[1]))
            img = cv2.circle(img, pi, 4, (0,0,255), -1) 

        ## bbx
        rcx, rcy, rw, rh = read_pts_file(lp,w,h)[1:5]
        lux, luy, rbx, rby = round((rcx - rw/2)*w), round((rcy - rh/2)*h), round((rcx + rw/2)*w), round((rcy + rh/2)*h)
        cv2.rectangle(img, (lux, luy), (rbx, rby), (255, 0, 0), 2)

        cv2.imshow('Image', img)
        # Wait for a key press and then close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """

        
        # Specify the file path
        op = labelPath + imn[:-3] + 'txt'

        # write file
        
        with open(op, 'w') as f:
            # Iterate through the list and write each element to a new line in the file
            for di in read_pts_file(lp, w, h):
                f.write(str(di) + ' ')