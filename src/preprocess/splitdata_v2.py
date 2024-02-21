import os
from sklearn.model_selection import train_test_split
import shutil

datafolderPath = '/home/wish/UoM/0thers/IEEE_ICME_2024_Grand_Challenges/ivslab_facial_train_filtered/'
datafolderList = os.listdir(datafolderPath)
datafolderList = sorted(datafolderList)

for foldern in datafolderList:

    print('-' * 20, foldern, '-' * 20)

    folderp = datafolderPath + foldern + '/'

    # Define paths to your data folders
    images_folder = folderp + 'images/'
    labels_folder = folderp + 'labels/'

    output_folder = './data_filtered/'
    output_images_folder = output_folder + 'images/'
    output_labels_folder = output_folder + 'labels/'

    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_images_folder, exist_ok=True)
    os.makedirs(output_labels_folder, exist_ok=True)

    # Define paths for train and validation folders
    train_images_folder = os.path.join(output_images_folder, 'train')
    val_images_folder = os.path.join(output_images_folder, 'val')
    train_labels_folder = os.path.join(output_labels_folder, 'train')
    val_labels_folder = os.path.join(output_labels_folder, 'val')

    # Create train and validation folders if they don't exist
    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(val_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    os.makedirs(val_labels_folder, exist_ok=True)

    # Get the list of files in each folder
    image_files = sorted(os.listdir(images_folder))
    label_files = sorted(os.listdir(labels_folder))

    # Split the data into train and validation sets
    image_train, image_val, label_train, label_val = train_test_split(image_files, label_files, test_size=0.2, random_state=42)

    # Move images to train and val folders
    for image in image_train:
        shutil.copyfile(os.path.join(images_folder, image), os.path.join(train_images_folder, foldern + '_' + image))
    for image in image_val:
        shutil.copyfile(os.path.join(images_folder, image), os.path.join(val_images_folder, foldern + '_' + image))

    # Move labels to train and val folders
    for label in label_train:
        shutil.copyfile(os.path.join(labels_folder, label), os.path.join(train_labels_folder, foldern + '_' + label))
    for label in label_val:
        shutil.copyfile(os.path.join(labels_folder, label), os.path.join(val_labels_folder, foldern + '_' + label))