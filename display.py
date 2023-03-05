import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

img_data = rasterio.open('/home/shezin/Desktop/Flood Estimation/example_highlighted.tif')
#img_data = rasterio.open('/home/shezin/Desktop/Flood Estimation/srm/submss_srm.tif')
fig, ax = plt.subplots(figsize=(10,10))    
show(img_data)