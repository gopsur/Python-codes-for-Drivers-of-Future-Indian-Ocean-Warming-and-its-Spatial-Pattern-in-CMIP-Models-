    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: gopika.s
"""

dname2 = "Yearly"

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("ata_call_dyn.py")

###### CMIP SST CHAnge MMMM ######
def plot(x,xname,level,cmap):
  lon1 = mask1["lon"]
  lat1 = mask1["lat"]
  lon2d, lat2d = np.meshgrid(lon1, lat1)
  xticks = ([30 ,  60, 90])
  yticks = ([-20.,  0, 20])
  fig = plt. figure(figsize=[6.5,5])
  ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                       (central_longitude=180),facecolor=('white'))
  plt.contourf(lon2d, lat2d, x ,extend='both',
               levels=level,
               transform=ccrs.PlateCarree(),
               cmap=cmap)
  ax.coastlines(color='white')
  plt.colorbar(location='bottom', pad=0.1, shrink=.9)
  plt.title(f'{xname}')
  land = cfeature.NaturalEarthFeature('physical', 'land', \
                                      scale='110m', edgecolor='k', 
                                      facecolor=cfeature.COLORS['land'])
  ax.add_feature(land, facecolor='white')


  ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
  
  # xs = [-10, 15, 15, -10, -10]
  # ys = [-140, -140, -115, -115, -140]
  # ax.plot( ys, xs, color="green")
  # xs = [-13, 3, 3, -13, -13]
  # ys = [-95, -95, -75, -75, -95]
  # ax.plot( ys, xs, color="green")

  plt.savefig(xname+'.eps', format='eps', dpi=500)



name = 'lhf feedback MMM'
plot(lhf_feed_MMM,name,np.arange(4,17,1),'Reds')

name = 'LWu Feedback MMM'
plot(lwup_feed_MMM,name,np.arange(4,17,1),'Reds')

name = 'LWd Feedback MMM'
plot(tot_lwd_feed_MMM,name,np.arange(-16,-3,1),'Blues_r')

name = 'LWu+LHF Feedback MMM'
plot(lwup_feed_MMM+lhf_feed_MMM,name,np.arange(4,17,1),'Reds')

name = 'alpha MMM'
plot(alpha_MMM,name,np.arange(4,17,1),'Reds')


#########################################################################
###### intermodel STD alpha ######

alpha_std = alpha.std("sfc")
alpha_mean_MMM=alpha_MMM.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
std_per_of_MMM = (alpha_std/alpha_mean_MMM)*100
name = '% of Alpha Multi-Model STD' 
plot(std_per_of_MMM,name,np.arange(4,17,1),'YlGnBu')









