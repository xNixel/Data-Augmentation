import cv2
import os
import random

def zoom_mobile_camera(image, zoom_factor, zoom_direction):

    # Get image dimensions
    height, width = image.shape[:2]
    
    if zoom_direction == "in":
        # Calculate new dimensions after zoom in
        new_height = int(height / zoom_factor)
        new_width = int(width / zoom_factor)
        
        # Calculate padding values
        top_pad = max((height - new_height) // 2, 0)
        bottom_pad = max(height - new_height - top_pad, 0)
        left_pad = max((width - new_width) // 2, 0)
        right_pad = max(width - new_width - left_pad, 0)
        
        # Resize the image to the new dimensions
        zoomed_image = cv2.resize(image, (new_width, new_height))
        
        # Pad the zoomed image to match the original image dimensions
        zoomed_image = cv2.copyMakeBorder(zoomed_image, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    else:
        # Calculate new dimensions after zoom out
        new_height = int(height * zoom_factor)
        new_width = int(width * zoom_factor)
        
        # Resize the image to the new dimensions
        zoomed_image = cv2.resize(image, (new_width, new_height))
        
        # Crop the zoomed image to match the original image dimensions
        top_crop = max((new_height - height) // 2, 0)
        bottom_crop = max(new_height - height - top_crop, 0)
        left_crop = max((new_width - width) // 2, 0)
        right_crop = max(new_width - width - left_crop, 0)
        zoomed_image = zoomed_image[top_crop:top_crop+height, left_crop:left_crop+width]
    
    return zoomed_image

# Directory containing your original images
input_dir = ''
output_dir = ''

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Range for the zoom factor
zoom_factor_range = (0.5, 1.1)  # Adjust this range as needed

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    # Load the image
    image_path = os.path.join(input_dir, filename)
    image = cv2.imread(image_path)
    
    # Generate a random zoom factor within the specified range
    zoom_factor = random.uniform(*zoom_factor_range)
    
    # Randomly choose zoom direction
    zoom_direction = random.choice(["in", "out"])
    
    # Apply zoom effect
    zoomed_image = zoom_mobile_camera(image, zoom_factor, zoom_direction)
    
    # Save the zoomed image to the output directory
    output_filename = f"{os.path.splitext(filename)[0]}_zoom_{zoom_direction}.jpg"
    output_path = os.path.join(output_dir, output_filename)
    cv2.imwrite(output_path, zoomed_image)

print("Augmentation complete!")
