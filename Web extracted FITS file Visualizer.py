# Web extracted FITS file Visualizer

import numpy as np

# Set up matplotlib
import matplotlib
import matplotlib.pyplot as plt


from astropy.io import fits

# Downloads FITS file
from astropy.utils.data import download_file
image_file = download_file('https://fits.gsfc.nasa.gov/samples/FOCx38i0101t_c0f.fits', cache=True ) # To use your own data in the future, use astropy.io.fits.open()

# Opens the FITS file to find out what it contains
hdu_list = fits.open(image_file)
hdu_list.info()

image_data = hdu_list[0].data # Data stored as a 2D numpy array

# Looks at shape of the array
print(type(image_data)) # Show the Python type for image_data
print(image_data.shape) # Show the number of pixels per side in the 2-D image

# Close FITS file to ensure that it won't continue using up excess memory or file handles on the computer
hdu_list.close()

# If you don't need to examine the FITS header, you can call fits.getdata to bypass the previous steps
# image_data = fits.getdata(image_file)

plt.imshow(image_data)
plt.colorbar()
plt.show()

# To see more color maps
# http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps

# Shows basic statistics
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))