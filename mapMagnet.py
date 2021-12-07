import pyIGRF
import numpy as np
import matplotlib.pyplot as plt

latR = 100
lonR = 100
ano=1999

lat = np.linspace(-90, 90, latR)
lon = np.linspace(-180, 180, lonR)#240,390

mag = np.zeros([latR,lonR])

for lat0 in range(0,latR):
    for lon0 in range(0,lonR):
        
        mag[lat0,lon0] = pyIGRF.igrf_value(lat[lat0], lon[lon0], year=ano)[6]


plt.figure(figsize=(20,4))
plt.contourf(lon,lat,mag, levels=15, cmap='gist_ncar')
cb=plt.colorbar()
cb.set_label('nT')
plt.title('Anomalia magnética do Atlântico Sul ({})'.format(ano))
plt.axis([-180, 180, -90, 90])
#plt.ylim(-95, 95, 15)
#plt.xlim(-185, 185, 15)
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('{}'.format(ano))
plt.show()