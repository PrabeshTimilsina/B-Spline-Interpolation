import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from grayScaleImage import grayScaleimage
from inerpolateimage import controlpoints,knots,bsplininterpolation

# Get the image file path from the user
image_path = input("Enter the path to the image file: ")

# Load the original image
original_image = mpimg.imread(image_path)

#grayscale image
grayscale_img= grayScaleimage(original_image)

#control points 
contrl_pts=controlpoints(grayscale_img)

#knots
knots=knots(grayscale_img,10)

#interpolate image
interpolated_img=bsplininterpolation(contrl_pts,knots,3)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))

# Display the original image in the left subplot
ax1.imshow(original_image)
ax1.set_title('Original Image')

# Display the loaded image in the right subplot
ax2.imshow(interpolated_img)
ax2.set_title('Loaded Image')

# Show the figure
plt.show()