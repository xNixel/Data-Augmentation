import cv2
import numpy as np
import os

def random_brightness(image, brightness_range=(-20, 20), min_brightness=10):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    augmented_images = []
    
    for _ in range(num_variations):
        # Generate a random brightness value within the specified range
        brightness = np.random.randint(brightness_range[0], brightness_range[1] + 1)
        
        # Calculate the current brightness level of the image
        current_brightness = np.mean(hsv[:, :, 2])
        
        # Adjust the brightness range dynamically to prevent the image from becoming too dark
        if brightness < 0 and current_brightness < min_brightness:
            brightness_range = (min_brightness - current_brightness, brightness_range[1])
        
        # Apply the brightness adjustment to the Value channel
        hsv[:, :, 2] = np.clip(hsv[:, :, 2].astype(np.int32) + brightness, 0, 255).astype(np.uint8)
        
        # Convert the image back to the BGR color space and append to the list
        augmented_images.append(cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR))
    
    return augmented_images

# Directory containing your original images
input_dir = ''
output_dir = ''
num_variations = 50  # Number of variations for each image

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    # Load the image
    image_path = os.path.join(input_dir, filename)
    image = cv2.imread(image_path)
    
    # Apply random brightness adjustment multiple times
    augmented_images = random_brightness(image)
    
    # Save the augmented images to the output directory
    for i, augmented_image in enumerate(augmented_images):
        output_filename = f"{os.path.splitext(filename)[0]}_brightness_{i}.jpg"
        output_path = os.path.join(output_dir, output_filename)
        cv2.imwrite(output_path, augmented_image)

print("Augmentation complete!")