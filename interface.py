import matplotlib.pyplot as plt
from grayScaleImage import grayScaleimage
from inerpolateimage import quadratic_b_spline, interpolate_matrix
from PIL import Image
import numpy as np

# Get the image file path from the user
image_path = input("Enter the path to the image file: ")

# Load the original image
original_image = Image.open(image_path)

#grayscale image
grayscale_img= original_image.convert("L")


input_matrix = np.array(grayscale_img)

# Define desired output shape
out_shape = (100, 100)

interpolated_matrix = interpolate_matrix(input_matrix, out_shape)

interpolated_image = Image.fromarray(interpolated_matrix.astype(np.uint8))

interpolated_image.save("output.jpg")

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

# Display the original image in the left subplot
ax1.imshow(original_image)
ax1.set_title('Original Image')

# Display the loaded image in the right subplot
ax2.imshow(interpolated_image)
ax2.set_title('Loaded Image')

# Show the figure
plt.show()