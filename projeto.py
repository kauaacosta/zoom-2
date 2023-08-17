import cv2
import numpy as np

# Load an image using OpenCV
image_path = 'train/damage/image (1).jpeg'
original_image = cv2.imread(image_path)

# Define zoom factor and perform zoom augmentation
zoom_factor = 3.5
zoomed_image = cv2.resize(original_image, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)

# Perform horizontal flip augmentation
flipped_image = cv2.flip(original_image, 1)  # 1 for horizontal flip

# Display the original and augmented images
cv2.imshow('Original Image', original_image)
cv2.imshow('Zoomed Image', zoomed_image)
cv2.imshow('Flipped Image', flipped_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()