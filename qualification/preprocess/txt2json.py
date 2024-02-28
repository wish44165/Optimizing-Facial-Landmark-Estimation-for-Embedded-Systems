import os
import json
import cv2

class_dict = {
    0: "face", 1: "new_face"
}
def txt_to_json(txt_file, image_file):
    # Read the image
    image = cv2.imread(image_file)
    image_height, image_width, _ = image.shape

    # Initialize an empty list to store shapes
    shapes = []

    # Read lines from the text file
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            data = line.split()
            class_id = int(data[0])
            x_center = float(data[1]) * image_width
            y_center = float(data[2]) * image_height
            w = float(data[3]) * image_width
            h = float(data[4]) * image_height

            x_min = x_center - w / 2
            y_min = y_center - h / 2
            x_max = x_center + w / 2
            y_max = y_center + h / 2

            # Define the bounding box as a list of four points
            bbox = [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]]

            # Add the rectangle shape to the list
            shapes.append({
                "label": class_dict[class_id],
                "points": bbox,
                "group_id": i,
                "description": None,
                "difficult": False,
                "shape_type": "rectangle",
                "flags": None,
                "attributes": {}
            })

            # Parse the key points (landmarks)
            for j in range(5, len(data), 3):
                x = float(data[j]) * image_width
                y = float(data[j + 1]) * image_height
                v = float(data[j + 2])
                if v == 2:
                    non_vis = False
                else:
                    non_vis = True
                class_id = str((j - 5) // 3)
                # Add each key point as a shape to the list
                shapes.append({
                    "label": class_id,
                    "points": [[x, y]],
                    "group_id": i,
                    "description": None,
                    "difficult": non_vis,
                    "shape_type": "point",
                    "flags": None,
                    "attributes": {}
                })

    # Define the JSON data structure
    json_data = {
        "version": "2.3.1",
        "flags": {},
        "shapes": shapes,
        "imagePath": os.path.basename(image_file),
        "imageData": None,
        "imageHeight": image_height,
        "imageWidth": image_width
    }

    return json_data

def folder_to_json(txt_folder, image_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Iterate over the text files in the specified folder
    for txt_file in os.listdir(txt_folder):
        if txt_file.endswith('.txt'):
            # Determine the corresponding image file path
            image_file = os.path.join(image_folder, os.path.splitext(txt_file)[0] + '.jpg')
            if not os.path.exists(image_file):
                image_file = os.path.join(image_folder, os.path.splitext(txt_file)[0] + '.png')
            # Convert the text file to JSON format
            json_data = txt_to_json(os.path.join(txt_folder, txt_file), image_file)
            # Define the output JSON file path
            output_file = os.path.join(output_folder, os.path.splitext(txt_file)[0] + '.json')
            # Write the JSON data to the output file
            with open(output_file, 'w') as f:
                json.dump(json_data, f, indent=4)

# Input folder containing text files with labels
txt_folder = '../../datasets/v0/semi_labels/'
# Folder containing corresponding images
image_folder = '../../datasets/v0/images/'
# Output folder for JSON files
output_folder = '../../datasets/v0/semi_json_labels'

# Convert text labels to JSON format
folder_to_json(txt_folder, image_folder, output_folder)
