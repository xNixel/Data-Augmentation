import cv2
import numpy as np
import os

def add_mobile_camera_noise(image, intensity=0.01, high_end=False):
    """
    Add noise resembling typical noise found in images from mobile devices.
    
    Parameters:
        image (numpy.ndarray): Input image.
        intensity (float): Intensity of the noise. Default is 0.01.
        high_end (bool): Whether to simulate noise from a high-end device. Default is False.
        
    Returns:
        numpy.ndarray: Image with noise added.
    """
    # Add Gaussian noise with specified intensity
    noise = np.random.normal(0, intensity, image.shape).astype(np.float32)
    noisy_image = cv2.add(image, noise, dtype=cv2.CV_8U)  # Specify output data type as uint8
    
    if not high_end:
        # Add salt-and-pepper noise for low-end devices
        salt_pepper_noise = np.random.rand(*image.shape)
        noisy_image[salt_pepper_noise < 0.02] = 0
        noisy_image[salt_pepper_noise > 0.98] = 255
    
    return noisy_image

# Directory containing your original images
input_dir = ''
output_dir = ''

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Number of variations for each image
num_variations = 20

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    # Load the image
    image_path = os.path.join(input_dir, filename)
    image = cv2.imread(image_path)
    
    # Apply noise augmentation multiple times
    for i in range(num_variations):
        # Add noise resembling noise from mobile devices
        noisy_image_low_end = add_mobile_camera_noise(image, intensity=0.01, high_end=False)
        noisy_image_high_end = add_mobile_camera_noise(image, intensity=0.005, high_end=True)
        
        # Save the noisy images to the output directory
        output_filename_low_end = f"{os.path.splitext(filename)[0]}_low_end_noise_{i}.jpg"
        output_filename_high_end = f"{os.path.splitext(filename)[0]}_high_end_noise_{i}.jpg"
        
        output_path_low_end = os.path.join(output_dir, output_filename_low_end)
        output_path_high_end = os.path.join(output_dir, output_filename_high_end)
        
        cv2.imwrite(output_path_low_end, noisy_image_low_end)
        cv2.imwrite(output_path_high_end, noisy_image_high_end)

print("Augmentation complete!")
