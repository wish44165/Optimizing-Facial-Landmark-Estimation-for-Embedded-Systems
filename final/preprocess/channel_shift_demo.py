import cv2
import numpy as np

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
    print(b_shift, g_shift, r_shift)

    # Ensure shifted values don't exceed 255 or fall below 0
    shifted_image[:, :, 0] = np.clip(shifted_image[:, :, 0] + b_shift, 0, 255)
    shifted_image[:, :, 1] = np.clip(shifted_image[:, :, 1] + g_shift, 0, 255)
    shifted_image[:, :, 2] = np.clip(shifted_image[:, :, 2] + r_shift, 0, 255)

    return shifted_image.astype(np.uint8)


# dataset path
datasetPath = '/home/wish/pro/ICME2024/datasets/f1/'

# Load an image
image_path ='/home/wish/pro/ICME2024/datasets/f1/images/train/0001.png'
image = cv2.imread(image_path)

# Apply random channel shift
shifted_image = channel_shift(image)

# Display original and shifted images
cv2.imshow('Original Image', image)
cv2.imshow('Shifted Image', shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
