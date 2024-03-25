import os
import cv2
import sys
import shutil
import numpy as np

np.random.seed(43)

def channel_shift(image):
    """
    Apply random channel shift to the input image.

    Parameters:
        image: numpy.ndarray
            Input image.

    Returns:
        numpy.ndarray
            Image with applied random channel shift.
    """
    shifted_image = image.copy().astype(np.float32)
    b_shift = np.random.randint(-20, 21)  # Random shift for blue channel (-50 to 50)
    g_shift = np.random.randint(-20, 21)  # Random shift for green channel (-50 to 50)
    r_shift = np.random.randint(-20, 21)  # Random shift for red channel (-50 to 50)

    # Ensure shifted values don't exceed 255 or fall below 0
    shifted_image[:, :, 0] = np.clip(shifted_image[:, :, 0] + b_shift, 0, 255)
    shifted_image[:, :, 1] = np.clip(shifted_image[:, :, 1] + g_shift, 0, 255)
    shifted_image[:, :, 2] = np.clip(shifted_image[:, :, 2] + r_shift, 0, 255)

    return shifted_image.astype(np.uint8)

f1Path = '/home/wish/pro/ICME2024/datasets/f1/'
f1ImagePath = f1Path + 'images/'
f1LabelPath = f1Path + 'labels/'
f1ImageList = os.listdir(f1ImagePath)
f1ImageList = sorted(f1ImageList)
#print(f1ImageList)    # ['train', 'val']

f2Path = '/home/wish/pro/ICME2024/datasets/f2/'
f2ImagePath = f2Path + 'images/'
f2LabelPath = f2Path + 'labels/'
os.makedirs(f2Path, exist_ok=True)
os.makedirs(f2ImagePath, exist_ok=True)
os.makedirs(f2LabelPath, exist_ok=True)
f2ImageList = os.listdir(f2ImagePath)
f2ImageList = sorted(f2ImageList)

for foldern in f1ImageList:
    imagePath = f1ImagePath + foldern + '/'
    imageList = os.listdir(imagePath)
    imageList = sorted(imageList)

    labelPath = f1LabelPath + foldern + '/'
    for imgn in imageList:
        ip = imagePath + imgn
        lp = labelPath + imgn[:-3] + 'txt'

        f2ImagePathFolder = f2ImagePath + foldern + '/'
        f2LabelPathFolder = f2LabelPath + foldern + '/'
        os.makedirs(f2ImagePathFolder, exist_ok=True)
        os.makedirs(f2LabelPathFolder, exist_ok=True)

        # original
        dst_ip = f2ImagePathFolder + imgn
        dst_lp = f2LabelPathFolder + imgn[:-3] + 'txt'
        shutil.copy(ip, dst_ip)
        shutil.copy(lp, dst_lp)

        # shifted
        image = cv2.imread(ip)
        shifted_image = channel_shift(image)

        dst_ip = f2ImagePathFolder + imgn[:-4] + '_cs' + imgn[-4:]
        dst_lp = f2LabelPathFolder + imgn[:-4] + '_cs.txt'

        cv2.imwrite(dst_ip, shifted_image)
        shutil.copy(lp, dst_lp)