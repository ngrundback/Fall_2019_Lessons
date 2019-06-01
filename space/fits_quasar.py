#!/usr/bin/python3

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

hdulist = fits.open('blue.fits')
print(hdulist.info())
data = hdulist[0].data
print(data.shape)

# Plot the 2D array
plt.imshow(data, cmap=plt.cm.viridis)
plt.xlabel('x-pixels (RA)')
plt.ylabel('y-pixels (Dec)')
plt.colorbar()
plt.show()
