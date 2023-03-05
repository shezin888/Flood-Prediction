from PIL import Image
import numpy
# Load the TIFF image
im = Image.open('/home/shezin/Desktop/Flood Estimation/srm/band08.tif')



# Convert the image to a numpy array
im_arr = numpy.array(im)


# Define the color you want to use to highlight the parts with certain values
highlight_color = [255, 0, 0]  # Red color

# Define the threshold value for the parts you want to highlight
threshold = 123

# Iterate over each pixel in th+e array and set the color of the parts with certain values
for i in range(im_arr.shape[0]):
    for j in range(im_arr.shape[1]):
        if im_arr[i,j] >=5 and im_arr[i,j] <=8:
            im_arr[i,j] = 1000

# Convert the numpy array back to an image
im = Image.fromarray(im_arr)

# Save the modified image
im.save('example_highlighted.tif')