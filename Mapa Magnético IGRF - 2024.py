import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pyIGRF

latR = 800 ; lonR = 800 ; ano = 2024

lat = np.linspace(-90, 90, latR)
lon = np.linspace(-180, 180, lonR)

lon_grid, lat_grid = np.meshgrid(lon, lat)

mag = np.zeros([latR, lonR])

for lat0 in range(latR):
    for lon0 in range(lonR):
        mag[lat0, lon0] = pyIGRF.igrf_value(lat[lat0], lon[lon0], year=ano)[6]

plt.figure(figsize=(24, 16))

# Plot do mapa de projeção robin
m = Basemap(projection='robin', lon_0=0, resolution='c')
m.drawcoastlines()
m.drawcountries()
parallels = np.arange(-90., 90, 18.)
m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=16)
meridians = np.arange(-180., 180., 36.)
m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=16)
plt.title('Mapa de projeção Robin')

# Sobrepor a anomalia magnética no mapa de projeção robin
x, y = m(lon_grid, lat_grid)
m.contourf(x, y, mag, levels=15, cmap='gist_ncar', alpha=0.85)

cb = m.colorbar(location='bottom', pad='10%')
cb.set_label('nT')

plt.title('Anomalia magnética do Atlântico Sul ({})'.format(ano), fontsize=24)

plt.savefig('{}_mapa.png'.format(ano))
plt.show()
