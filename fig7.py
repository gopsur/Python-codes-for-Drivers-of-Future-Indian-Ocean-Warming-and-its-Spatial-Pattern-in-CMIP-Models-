import numpy as np
from scipy import signal
import numpy.polynomial.polynomial as poly
from netCDF4 import Dataset

import matplotlib.pyplot as plt
from eofs.standard import Eof
import seaborn as sns
from scipy import stats

dname2 = "Yearly"

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")
###### RSST intermodel diversity and RSST change####

def plot2(x,xname,level,cmap):
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
  cs = plt.contour(lon2d, lat2d, zh_T_pert_MMM,transform=ccrs.PlateCarree(),colors='k',linewidths=1)
  ax.clabel(cs, cs.levels, inline=True, fontsize=10)
  ax.add_feature(land, facecolor='white')
  ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
  plt.savefig(xname+'.eps', format='eps', dpi=500)



rsst_ch_pert_std = rsst_ch_pert.std("sfc")
name = 'Recon_RSST_std + RSST change'
plot2(rsst_ch_pert_std,name,np.arange(0,.33,.03),'YlGnBu')
###### EOF analysis ######

from eofs.xarray import Eof
rsst_ch_pert_no_time = rsst_ch_pert.drop('time')
rsst_ch_pert_rename = rsst_ch_pert_no_time.rename({'sfc': 'time'})


solver = Eof(rsst_ch_pert_rename)

pcs = solver.pcs(npcs=3, pcscaling=0)
eofs = solver.eofs(neofs=3, eofscaling=0)
eigenvalue1 = solver.eigenvalues(neigs=3)
variance_fractions = solver.varianceFraction(neigs=3)
total_variance = solver.totalAnomalyVariance()



pc1= pcs[:,0]
pc1 = pc1.rename({'time': 'sfc'})
pc1_normalized = (pc1 ) / pc1.std()
pc2 = pcs[:,1]
pc2 = pc2.rename({'time': 'sfc'})
pc2_normalized = (pc2 ) / pc2.std() *-1

#eof1 map

def linear_trend(x, y):
    pf = np.polyfit(x, y, 1)
    return xr.DataArray(pf[0])

slopes_u = xr.apply_ufunc(linear_trend,
                          pc1_normalized, tauu_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

slopes_v = xr.apply_ufunc(linear_trend,
                          pc1_normalized, tauv_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

slopes_clt = xr.apply_ufunc(linear_trend,
                          pc1_normalized, clt_ch,
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

plt.contourf(lon2d, lat2d, (eofs[0]*pc1.std()),extend='both',
              levels=np.arange(-.2,.225,.025),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'(c) RSST changes{dname2} (EoF, {variance_fractions[0]*100:.1f}%)')

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')
u=(slopes_u[::4,::4]).values
v=(slopes_v[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="k", width=0.003, scale_units='xy', scale=0.001)

plt.quiverkey(Q,.02, -.1,.001,str(.001)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, slopes_clt,transform=ccrs.PlateCarree(),colors='green',linewidths=1.5)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
xs = [-10, 15, 15, -10, -10]
ys = [-140, -140, -115, -115, -140]
ax.plot( ys, xs, color="blue")
xs = [-13, 3, 3, -13, -13]
ys = [-95, -95, -75, -75, -95]
ax.plot( ys, xs, color="blue")
xs = [-5, 5, 5, -5, -5]
ys = [-135, -135, -80, -80, -135]
ax.plot( ys, xs, color="green")
plt.savefig('rsst_ch_pert_eof1_'+dname2+'.png',  dpi=300)

#eof2 map
slopes_u = xr.apply_ufunc(linear_trend,
                          pc2_normalized, tauu_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

slopes_v = xr.apply_ufunc(linear_trend,
                          pc2_normalized, tauv_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

slopes_windspeed = xr.apply_ufunc(linear_trend,
                          pc2_normalized, sfcWind_ch,
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

plt.contourf(lon2d, lat2d, (eofs[1]*-1*pc2.std()),extend='both',
              levels=np.arange(-.2,.225,.025),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'(c) RSST changes{dname2} (EoF, {variance_fractions[1]*100:.1f}%), winds, windspeedchange')

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')
u=(slopes_u[::4,::4]).values
v=(slopes_v[::4,::4]).values
Q=plt.quiver(lon1[::4].values, lat1[::4].values, u, v, transform=ccrs.PlateCarree(), color="k", width=0.003, scale_units='xy', scale=0.001)

plt.quiverkey(Q,.02, -.1,.001,str(.001)+' N/m\u00b2',labelpos='E',coordinates='axes')
cs = plt.contour(lon2d, lat2d, slopes_windspeed,transform=ccrs.PlateCarree(),colors='green',linewidths=1.5)
ax.clabel(cs, inline=True, fontsize=10)
ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
xs = [-10, 25, 25, -10, -10]
ys = [-140, -140, -75, -75, -140]
ax.plot( ys, xs, color="blue")
xs = [-10, -20, -20, -10, -10]
ys = [-140, -140, -75, -75, -140]
ax.plot( ys, xs, color="blue")

plt.savefig('rsst_ch_pert_eof2_'+dname2+'.png',  dpi=300)

#scatter plots

zonal_wind_change_EQIO = tauu_ch.sel(lon=loneq,lat=lateq).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
mgradext_tauv_ch = tauv_ch.sel(lon=lon_mgradext,lat=lat_mgradext).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

def scatter(xl, yl, x, y, xlab, ylab, reg, gap, gap1, savename):
    x = x.values if hasattr(x, 'values') else x
    y = y.values if hasattr(y, 'values') else y
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.xlim(xl)
    plt.ylim(yl)
    pp = ax.scatter(x, y, c='dimgray', marker='o', s=30, label='Data Points')
    sns.regplot(x=x, y=y, scatter=False, color='green', ci=95)
    sns.regplot(x=x, y=y, scatter=False, color='Black', x_ci=None, ci=0)
    ax.set_xlabel(f'{xlab}', fontsize=14)
    ax.set_ylabel(f'{ylab}', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.6)
    corr_coefficient = np.corrcoef(x, y)[0, 1]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(slope, intercept, r_value, p_value, std_err)
    ax.tick_params(axis='both', which='both', labelsize=12)
    plt.axhline(y=0, color='orange', linestyle=':')
    plt.axvline(x=0, color='orange', linestyle=':')
    ax.scatter(np.mean(x), np.mean(y), c='red', marker='*', s=100, label='Mean Point')
    ax.set_title(f'{xlab} vs. {ylab} {reg}; R={corr_coefficient:.2f}', fontsize=16)
    ax.tick_params(axis='both', which='both', labelsize=12)
    plt.savefig('fig_' + savename + '_' + reg + '.eps', format='eps', dpi=500)
    plt.show()


# PC1 vs Equatorial Zonal wind
scatter((-.02, .02), (-2.5, 2.5), zonal_wind_change_EQIO, pc1_normalized,
        f'{dname2} Zonal wind EQIO', 'EQGRAD_region', 'PC1 (normalised)', 1, .005,
        ''+dname2+'_PC1_vs_EQIO_tauu_changes')

# PC2 vs meridional wind
scatter((-0.02,0.02), (-2.5, 2.5), mgradext_tauv_ch, pc2_normalized,
        'basin ave tauv changes', '', 'PC2 (normalised)', 10, .001,
        ''+dname2+'_PC2_vs_IOave_tauvchanges')

