from curses import meta
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
dataset = gdal.Open(r'/home/shezin/Desktop/Flood Estimation/srm/submss_srm.tif')

band1 = dataset.GetRasterBand(4)
# print(meta.band1)
b1 = band1.ReadAsArray()

print(b1)
img = b1
f = plt.figure()
plt.imshow(img)
plt.savefig('sampplle.png')
plt.show()