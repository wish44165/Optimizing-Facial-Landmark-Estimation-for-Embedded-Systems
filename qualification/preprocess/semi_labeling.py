import os

def merge_labels(original_labels_folder, additional_labels_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files in the original labels folder
    for file_name in os.listdir(original_labels_folder):
        if file_name.endswith(".txt"):
            # Build file paths for original and additional labels
            original_labels_file = os.path.join(original_labels_folder, file_name)
            additional_labels_file = os.path.join(additional_labels_folder, file_name)

            # Merge labels
            merged_labels = merge_single_file(original_labels_file, additional_labels_file)

            # Save merged labels to the output folder
            output_file = os.path.join(output_folder, file_name)
            save_labels(merged_labels, output_file)

            print('Merged labels saved to:', output_file)


def merge_single_file(original_labels, additional_labels):
    # Read original labels
    with open(original_labels, 'r') as file:
        original_data = file.readlines()
    original_boxes = [line.strip().split() for line in original_data]

    # If additional labels file doesn't exist, return original labels directly
    if not os.path.exists(additional_labels):
        return original_boxes

    # Read additional labels
    with open(additional_labels, 'r') as file:
        additional_data = file.readlines()
    additional_boxes = [line.strip().split() for line in additional_data]

    # Add new boxes to the original labels
    merged_boxes = original_boxes.copy()

    for box in additional_boxes:
        # Set the additional class_id to 1
        box[0] = '1'
        # Check for overlap with original boxes
        overlapping = False
        for orig_box in original_boxes:
            if calculate_iou(box[1:5], orig_box[1:5]) > 0.2:
                overlapping = True
                break
        # If no overlap, add the box to the original labels
        if not overlapping:
            merged_boxes.append(box)

    return merged_boxes


def calculate_iou(box1, box2):
    x1, y1, w1, h1 = map(float, box1)
    x2, y2, w2, h2 = map(float, box2)
    xmin1, ymin1, xmax1, ymax1 = x1 - w1/2, y1 - h1/2, x1 + w1/2, y1 + h1/2
    xmin2, ymin2, xmax2, ymax2 = x2 - w2/2, y2 - h2/2, x2 + w2/2, y2 + h2/2

    inter_area = max(0, min(xmax1, xmax2) - max(xmin1, xmin2)) * max(0, min(ymax1, ymax2) - max(ymin1, ymin2))
    box1_area = w1 * h1
    box2_area = w2 * h2
    iou = inter_area / (box1_area + box2_area - inter_area + 1e-5)  # Add 1e-5 to avoid division by zero

    return iou


def save_labels(labels, output_file):
    with open(output_file, 'w') as file:
        for box in labels:
            line = ' '.join(map(str, box)) + '\n'
            file.write(line)


def main():
    # Folder paths
    original_labels_folder = '../../datasets/v0/labels/'
    additional_labels_folder = r'D:\ultralytics\runs\facial\predict\labels'
    output_folder = '../../datasets/v0/semi_labels/'

    # Merge labels
    merge_labels(original_labels_folder, additional_labels_folder, output_folder)

if __name__ == "__main__":
    main()
