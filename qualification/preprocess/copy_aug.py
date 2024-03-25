import os
import shutil

COPYTIMES = 8

v4Path = '/home/wish/pro/ICME2024/datasets/conf_0.2/v4/'
v4ImagePath = v4Path + 'images/'
v4LabelPath = v4Path + 'labels/'
v4ImageList = os.listdir(v4ImagePath)
v4ImageList = sorted(v4ImageList)

v4x8Path = '/home/wish/pro/ICME2024/datasets/v4_x8/'
v4x8ImagePath = v4x8Path + 'images/'
v4x8LabelPath = v4x8Path + 'labels/'
os.makedirs(v4x8Path, exist_ok=True)
os.makedirs(v4x8ImagePath, exist_ok=True)
os.makedirs(v4x8LabelPath, exist_ok=True)
v4x8ImageList = os.listdir(v4x8ImagePath)
v4x8ImageList = sorted(v4x8ImageList)

for foldern in v4ImageList:
    imagePath = v4ImagePath + foldern + '/'
    imageList = os.listdir(imagePath)
    imageList = sorted(imageList)

    labelPath = v4LabelPath + foldern + '/'
    for imgn in imageList:
        ip = imagePath + imgn
        lp = labelPath + imgn[:-3] + 'txt'


        v4x8ImagePathFolder = v4x8ImagePath + foldern + '/'
        v4x8LabelPathFolder = v4x8LabelPath + foldern + '/'
        os.makedirs(v4x8ImagePathFolder, exist_ok=True)
        os.makedirs(v4x8LabelPathFolder, exist_ok=True)

        for i in range(COPYTIMES):
            dst_ip = v4x8ImagePathFolder + imgn[:-4] + '_' + str(i) + imgn[-4:]
            dst_lp = v4x8LabelPathFolder + imgn[:-4] + '_' + str(i) + '.txt'
            #print('=' * 80)
            #print(ip)
            #print(dst_ip)
            #print(lp)
            #print(dst_lp)
            shutil.copy(ip, dst_ip)
            shutil.copy(lp, dst_lp)