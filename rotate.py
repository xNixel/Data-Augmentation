import cv2
import os
import numpy as np

# Function to rotate image by any degree within the range of -180 to 180 degrees
def rotate_image(image_path, output_path, angle):
    # Read the image
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate the rotation center
    center = (width / 2, height / 2)

    # Perform the rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)

    # Save the rotated image
    cv2.imwrite(output_path, rotated_image)

# Path to your dataset directory
dataset_path = ""

# Path to the output directory where augmented images will be saved
output_path = ""

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Define the range of rotation angles (-180 to 180 degrees)
rotation_angles = range(-180, 181, 10)

# Iterate over each image in the dataset
for filename in os.listdir(dataset_path):
    # Construct the full path to the image
    image_path = os.path.join(dataset_path, filename)

    # Randomly decide whether to rotate the image or not
    if np.random.rand() < 1:
        # Iterate over each rotation angle
        for angle in rotation_angles:
            # Construct the output filename with the rotation angle
            output_filename = f"{os.path.splitext(filename)[0]}_rotated_{angle}.jpg"
            output_filepath = os.path.join(output_path, output_filename)

            # Rotate the image and save the rotated image
            rotate_image(image_path, output_filepath, angle)
    else:
        # If not rotating, simply copy the original image to the output directory
        output_filepath = os.path.join(output_path, filename)
        os.makedirs(output_path, exist_ok=True)
        os.system(f'copy "{image_path}" "{output_filepath}"')