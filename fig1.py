    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: gopika.s
"""
from matplotlib.colors import LinearSegmentedColormap

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")

#########################################################################

###### CMIP SST CHAnge MMMM ######
###### CMIP RSST CHAnge MMMM +wind + sla ######

new_cmap = LinearSegmentedColormap.from_list("",['ivory','gold','indianred','maroon'])

# Map plot
lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, CMIP_SST_change_MMM,extend='both',
              levels=np.arange(2.5,3.6,.1),
              transform=ccrs.PlateCarree(),
              cmap=new_cmap)
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'CMIP_SST_change_MMM')
u=(CMIP_tauu_change_MMM[::4,::4]).values
v=(CMIP_tauv_change_MMM[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="gray", width=0.004, scale_units='xy', scale=0.002)

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
plt.quiverkey(Q,.02, -.1,.01,str(.002)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, CMIP_pr_change_MMM,transform=ccrs.PlateCarree(),colors='gray',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')


ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
xs = [-10, 15, 15, -10, -10]
ys = [-140, -140, -115, -115, -140]
ax.plot( ys, xs, color="blue")
xs = [-13, 3, 3, -13, -13]
ys = [-95, -95, -75, -75, -95]
ax.plot( ys, xs, color="blue")
xs = [-10, 25, 25, -10, -10]
ys = [-140, -140, -75, -75, -140]
ax.plot( ys, xs, color="red")
xs = [-10, -20, -20, -10, -10]
ys = [-140, -140, -75, -75, -140]
ax.plot( ys, xs, color="red")
plt.savefig('fig-1a.eps', format='eps', dpi=500)




#box plot
#IO
sst_ch_io=sst_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
#ZGRAD
lon1=slice(85,105);lat1=slice(-13,3)
lon2=slice(40,65);lat2=slice(-10,15)
sst_ch_ew=sst_ch.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-sst_ch.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

#MGRAD
#NH 
lon3=slice(40,105);lat3=slice(0,25)
#SH
lon4=slice(40,105);lat4=slice(-20,-10)
sst_ch_ns=sst_ch.sel(lon=lon3,lat=lat3).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-sst_ch.sel(lon=lon4,lat=lat4).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)


fig, ax1 = plt.subplots()
ax1.set_ylim(0,5)

# Create a secondary y-axis
ax2 = ax1.twinx()
ax2.set_ylim( -1.1,1.1)
ax2.set_yticks([-1,-.5,0,.5,1])
# Boxplot
bp1 = ax1.boxplot(sst_ch_io, 0, '', positions=[0], widths=0.6, labels=['IO mean'], patch_artist=True)
bp2 = ax2.boxplot(sst_ch_ew, 0, '', positions=[1], widths=0.6, labels=['E-W gradient'], patch_artist=True)
bp3 = ax2.boxplot(sst_ch_ns, 0, '', positions=[2], widths=0.6, labels=['N-S gradient'], patch_artist=True)

# Set colors for the boxes
for box in bp1['boxes']:
 box.set(color='royalblue', linewidth=2)
 box.set(facecolor='cornflowerblue')

for box in bp2['boxes']:
 box.set(color='darkgreen', linewidth=2)
 box.set(facecolor='forestgreen')

for box in bp3['boxes']:
 box.set(color='red', linewidth=2)
 box.set(facecolor='red')
 
plt.title('Whisk IO mean and E-W N-S diversity in CMIP SST change')
plt.savefig('Whisk_diversity_SST.eps', format='eps',dpi=500)
plt.show()







