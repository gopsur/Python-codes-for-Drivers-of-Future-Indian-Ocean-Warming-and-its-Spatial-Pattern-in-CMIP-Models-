    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Created on Wed Feb  8 20:43:28 2023

@author: gopika.s
"""
from matplotlib.colors import LinearSegmentedColormap

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")

#########################################################################

#windspeed changes
lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, CMIP_sfcWind_change_MMM,extend='both',
              levels=np.arange(-.5,.55,.05),
              transform=ccrs.PlateCarree(),
              cmap='RdBu_r')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'CMIP_windspeed_change_MMM')

land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')
cs = plt.contour(lon2d, lat2d, delta_lhf_a.mean("sfc"),transform=ccrs.PlateCarree(),colors='black',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')


ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)


plt.savefig('fig-5a.eps', format='eps', dpi=500)


new_cmap = LinearSegmentedColormap.from_list("",['ivory','gold','indianred','maroon'])

#RH changes
lon1 = mask1["lon"]
lat1 = mask1["lat"]
lon2d, lat2d = np.meshgrid(lon1, lat1)
xticks = ([30 ,  60, 90])
yticks = ([-20.,  0, 20])
fig = plt. figure(figsize=[6.5,5])
ax = fig.add_subplot(111, projection=ccrs.PlateCarree
                      (central_longitude=180),facecolor=('white'))

plt.contourf(lon2d, lat2d, CMIP_hurs_change_MMM,extend='both',
              levels=np.arange(0,3.3,.3),
              transform=ccrs.PlateCarree(),
              cmap='OrRd')
ax.coastlines(color='white')
plt.colorbar(location='bottom', pad=0.1, shrink=.9)
plt.title(f'CMIP_RH_change_MMM')
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')

ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
cs = plt.contour(lon2d, lat2d, delta_lhf_a.mean("sfc"),transform=ccrs.PlateCarree(),colors='black',linewidths=1)
ax.clabel(cs, cs.levels, inline=True, fontsize=10)
land = cfeature.NaturalEarthFeature('physical', 'land', \
                                    scale='110m', edgecolor='k', 
                                    facecolor=cfeature.COLORS['land'])
ax.add_feature(land, facecolor='white')


ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)


plt.savefig('fig-5b.eps', format='eps', dpi=500)

##############################################
import seaborn as sns
from scipy import stats

dname2 = "Yearly"

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


LH_NTD_change = delta_lhf_a_mean

#scatter LH forcing vs RH
rh_change = hurs_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
scatter((0,3),(8,25),rh_change,LH_NTD_change,'RH Change','LHF NTD Change','IO_ocean',.1,1,'RH_Changes_vs_LHF_NTD_Changes')

#scatter LH forcing vs Windspeed
windspeed_change = sfcWind_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
scatter((-.40,.1),(8,25),windspeed_change,LH_NTD_change,'Windspeed Change','LHF NTD Change','IO_ocean',.1,1,'Windspeed_Changes_vs_LHF_NTD_Changes')


