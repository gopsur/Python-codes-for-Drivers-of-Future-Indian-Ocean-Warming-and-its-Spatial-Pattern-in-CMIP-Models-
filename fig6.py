    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Wed Feb  8 20:43:28 2023

@author: gopika.s
"""
import seaborn as sns
from scipy import stats


#here instead of full data, i saved the seasonal averaged data, and use this instead for time saving:
#so the data_call_JJAS.py and data_call_DJFM.py seasonal average datasets

#JJAS
execfile("data_call_JJAS.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def linear_trend(x, y):
  pf = np.polyfit(x, y, 1)
  return xr.DataArray(pf[0])

from matplotlib.colors import LinearSegmentedColormap
new_cmap = LinearSegmentedColormap.from_list("",['navy','deepskyblue','yellow','orange','red'])

#MMM climatological LH forcing

lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, hfls_pr.mean('sfc'),extend='both',
              levels=np.arange(-220,-60,20),
              transform=ccrs.PlateCarree(),
              cmap=new_cmap)
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'MMM LHF climatology JJAS')
u=(CMIP_tauu_pr_MMM[::4,::4]).values
v=(CMIP_tauv_pr_MMM[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.02)
plt.quiverkey(Q,.02, -.1,.1,str(.02)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, CMIP_sfcWind_pr_MMM,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)


plt.savefig('fig-MMM_LHF_climatology_JJAS.eps',format='eps',   dpi=300)

#MMM LH forcing changes

lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, delta_lhf_a.mean('sfc'),extend='both',
              levels=np.arange(-40,45,5),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'MMM LH FORCING JJAS')
u=(CMIP_tauu_change_MMM[::4,::4]).values
v=(CMIP_tauv_change_MMM[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.0015)
plt.quiverkey(Q,.02, -.1,.01,str(.0015)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, CMIP_sfcWind_change_MMM,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

plt.savefig('fig-delta_lhf_a_MMM_JJAS.eps',format='eps',   dpi=300)



#MMM LH forcing vs basin average LH forcing

slopes_u = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), tauu_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_v = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), tauv_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_spd = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), sfcWind_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_lhf = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), delta_lhf_a,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )



lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, slopes_lhf,extend='both',
              levels=np.arange(-9,10,1),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'regression_LHF_LHaMEAN_JJAS')
u=(slopes_u[::4,::4]).values
v=(slopes_v[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.001)
plt.quiverkey(Q,.02, -.1,.001,str(.001)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, slopes_spd,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

plt.savefig('fig-JJAS_reg__LHF_LHmeAN.eps', format='eps', dpi=300)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#DJFM
execfile("data_call_DJFM.py")
execfile("zl_method.py")
execfile("data_call_dyn_DJFM.py")

#MMM climatological LH forcing
lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, hfls_pr.mean('sfc'),extend='both',
              levels=np.arange(-220,-60,20),
              transform=ccrs.PlateCarree(),
              cmap=new_cmap)
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'MMM LHF climatology DJFM')
u=(CMIP_tauu_pr_MMM[::4,::4]).values
v=(CMIP_tauv_pr_MMM[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.02)
plt.quiverkey(Q,.02, -.1,.1,str(.02)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, CMIP_sfcWind_pr_MMM,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

plt.savefig('fig-MMM_LHF_climatology_DJFM.eps',format='eps',   dpi=300)

#MMM LH forcing changes
lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, delta_lhf_a.mean('sfc'),extend='both',
              levels=np.arange(-40,45,5),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'MMM LH FORCING DJFM')
u=(CMIP_tauu_change_MMM[::4,::4]).values
v=(CMIP_tauv_change_MMM[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.0015)
plt.quiverkey(Q,.02, -.1,.01,str(.0015)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, CMIP_sfcWind_change_MMM,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

plt.savefig('fig-delta_lhf_a_MMM_DJFM.eps',format='eps',   dpi=300)


#MMM LH forcing vs basin average LH forcing
slopes_u = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), tauu_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_v = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), tauv_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_spd = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), sfcWind_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )
slopes_lhf = xr.apply_ufunc(linear_trend,
                          delta_lhf_a_mean/delta_lhf_a_mean.std(), delta_lhf_a,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, slopes_lhf,extend='both',
              levels=np.arange(-9,10,1),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'regression_LHF_LHaMEAN_DJFM')
u=(slopes_u[::4,::4]).values
v=(slopes_v[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="darkblue", width=0.004, scale_units='xy', scale=0.001)
plt.quiverkey(Q,.02, -.1,.001,str(.001)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, slopes_spd,transform=ccrs.PlateCarree(),levels=10, colors='k',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)

plt.savefig('fig-djfm_reg__LHF_LHmeAN.eps', format='eps', dpi=300)
