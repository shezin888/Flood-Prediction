import rasterio as rio
import pandas as pd
import numpy as np

with rio.open('/home/shezin/Desktop/Flood Estimation/srm/band03_srm.tif') as dataset:
    val = dataset.read() # band 5
    no_data=dataset.nodata
    data = [(dataset.xy(x,y)[0],dataset.xy(x,y)[1],val[x,y]) for x,y in np.ndindex(val.shape) if val[x,y] != no_data]
    lon = [i[0] for i in data]
    lat = [i[1] for i in data]
    d = [i[2] for i in data]
    res = pd.DataFrame({"long":lon,'lat':lat,"data":d})
print(res.shape)
#print(res.max())



# import matplotlib.pyplot as plt
# from rasterio.plot import show
# fig, ax = plt.subplots(figsize=(8, 8))
# show(dataset.read(1), transform=dataset.transform,ax=ax)
# ax.plot(res.x,res.y,'ro', markersize=3)
 
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm
# import numpy as np

# plt.imsave('/home/shezin/Desktop/Flood Estimation/filename.png', np.array(res), cmap=cm.gray)
# plt.imshow(np.array(res))


############### Sorting ###############
df2 = res.sort_values("data")
print(df2)
#######################################


######################## Pandas dataframe to CSV ###############################
with open('/home/shezin/Desktop/Flood Estimation/srm/csv/lat_lon_data.csv', 'w') as csv_file:
    df2.to_csv(path_or_buf=csv_file)
################################################################################
