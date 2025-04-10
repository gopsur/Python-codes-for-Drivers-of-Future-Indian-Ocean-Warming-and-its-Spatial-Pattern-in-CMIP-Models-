    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Wed Feb  8 20:43:28 2023

@author: gopika.s
"""

dname2 = "Yearly"

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def plot(x,x1,xname,level,cmap,level2):
  lon1 = mask1["lon"]
  lat1 = mask1["lat"]
  lon2d, lat2d = np.meshgrid(lon1, lat1)
  xticks = ([30 ,  60, 90])
  yticks = ([-20.,  0, 20])
  fig = plt. figure(figsize=[6.5,5])
  ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                       (central_longitude=180),facecolor=('white'))

  plt.contourf(lon2d, lat2d, x,extend='both',
               levels=level,
               transform=ccrs.PlateCarree(),
               cmap=cmap)
  ax.coastlines(color='white')
  plt.colorbar(location='bottom', pad=0.1, shrink=.9)
  plt.title(f'{xname} {dname2}')
  # u=(CMIP_tauu_change_MMM[::4,::4]).values
  # v=(CMIP_tauv_change_MMM[::4,::4]).values
  # Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkslategray", width=0.004, scale_units='xy', scale=0.002)

  land = cfeature.NaturalEarthFeature('physical', 'land', \
                                      scale='110m', edgecolor='k', 
                                      facecolor=cfeature.COLORS['land'])
  ax.add_feature(land, facecolor='white')

  ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
  cs = plt.contour(lon2d, lat2d, x1,transform=ccrs.PlateCarree(),colors='black',linewidths=0.8,levels=level2)
  ax.clabel(cs, cs.levels, inline=True, fontsize=10)

  plt.savefig(xname+'.eps', format='eps', dpi=500)

    

########
#Heat flux forcing contribution
name = 'ZH_cont_delta_Hatm_pert_MMM'
plot(cont_delta_Hatm_pert_MMM,zh_T_pert_MMM,name,np.arange(-1.5,1.6,.1), 'RdBu_r',np.arange(-1.2,1.3,.1))

#Ocean dynamics contribution
name = 'ZH_cont_delta_Dyn_O_pert_MMM'
plot(cont_delta_Dyn_O_pert_MMM,zh_T_pert_MMM,name,np.arange(-1.5,1.6,.1), 'RdBu_r',np.arange(-1.2,1.3,.1))

#Heatflux feedback contribution
name = 'ZH_cont_feedback_ocean_MMM'
plot(cont_feedback_ocean_MMM,alpha_pert_MMM,name,np.arange(-1.5,1.6,.1), 'RdBu_r',np.arange(-2.5,3,.5))

#########
#Shortwave contribution
name = 'ZH_cont_rsntds_ch_pert_MMM'
plot(cont_rsntds_ch_pert_MMM,clt_ch_pert_MMM,name,np.arange(-1.5,1.6,.1), 'RdBu_r',np.arange(-5,6,1))

#LH forcing contribution
name = 'ZH_cont_delta_lhf_a_pert_MMM'
plot(cont_delta_lhf_a_pert_MMM,sfcWind_ch_pert_MMM,name,np.arange(-1.5,1.6,.1), 'RdBu_r',np.arange(-.35,.5,.15))


def plot(x,xname,level,cmap):
  lon1 = mask1["lon"]
  lat1 = mask1["lat"]
  lon2d, lat2d = np.meshgrid(lon1, lat1)
  xticks = ([30 ,  60, 90])
  yticks = ([-20.,  0, 20])
  fig = plt. figure(figsize=[6.5,5])
  ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                       (central_longitude=180),facecolor=('white'))

  plt.contourf(lon2d, lat2d, x,extend='both',
               levels=level,
               transform=ccrs.PlateCarree(),
               cmap=cmap)
  ax.coastlines(color='white')
  plt.colorbar(location='bottom', pad=0.1, shrink=.9)
  plt.title(f'{xname} {dname2}')
  land = cfeature.NaturalEarthFeature('physical', 'land', \
                                      scale='110m', edgecolor='k', 
                                      facecolor=cfeature.COLORS['land'])
  ax.add_feature(land, facecolor='white')

  ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

  plt.savefig(xname+'.eps', format='eps', dpi=500)


cont_delta_lw_a_pert_MMM= cont_delta_lwd_a_pert_MMM+cont_residue_lwu_pert_MMM

#LW forcing contribution
name = 'ZH_cont_delta_lw_a_pert_MMM'
plot(cont_delta_lw_a_pert_MMM ,name,np.arange(-1.5,1.6,.1), 'RdBu_r')




