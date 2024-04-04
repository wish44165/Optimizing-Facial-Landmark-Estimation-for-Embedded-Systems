import os

#imgPath = '/home/wish/pro/ICME2024/datasets/ivslab_facial_test_private_qualification/'
imgPath = './demo/'
imgList = os.listdir(imgPath)
imgList = sorted(imgList)

#print(imgList)

with open('./imageList.txt', 'w') as file:
    for imgn in imgList:
        ip = imgPath + imgn
        file.write(ip + '\n')