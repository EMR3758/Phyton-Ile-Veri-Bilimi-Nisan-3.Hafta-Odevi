import cv2
import numpy as np

# Read the image
image = cv2.imread('images.png')  

# Check if the image is loaded properly
if image is None:
    print("Image could not be loaded. Please check the file path.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Swap the Blue and Red channels
swapped_image = image.copy()
swapped_image[:, :, 0], swapped_image[:, :, 2] = image[:, :, 2].copy(), image[:, :, 0].copy()

# Convert the grayscale image to a 3-channel image
gray_image_3ch = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Combine images side by side
top_row = np.hstack((image, gray_image_3ch))
bottom_row = np.hstack((hsv_image, swapped_image))
combined_image = np.vstack((top_row, bottom_row))

# Write the name at the bottom of the combined image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(combined_image, 'Emir Ozcan', (10, combined_image.shape[0] - 30), 
            font, 2, (0, 0, 0), 3, cv2.LINE_AA)

# Display the result
cv2.imshow('Operations and Name', combined_image)

# Wait for 'q' key to be pressed and close the window
while True:
    kInp = cv2.waitKey(0)  
    if kInp == ord('q'):  
        print("q key pressed! Exiting...")
        cv2.destroyAllWindows()  
        break  
    else:
        print(f"Key {chr(kInp)} pressed. Window will not close.")
