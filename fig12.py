import numpy as np
from scipy import signal
import numpy.polynomial.polynomial as poly
from netCDF4 import Dataset

import matplotlib.pyplot as plt
from eofs.standard import Eof
import seaborn as sns
from scipy import stats
from scipy.stats import linregress
dname2 = "Yearly"

#instead of Indian Ocean here i loaded tropics,
#which are same CMIP models but only thing it extended full tropics
execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn_tropics.py")

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
pc2_normalized = (pc2 ) / pc2.std()*-1


def linear_trend(x, y):
    pf = np.polyfit(x, y, 1)
    return xr.DataArray(pf[0])





slopes_tropic_rsst_ch_pc1 = xr.apply_ufunc(linear_trend,
                          pc1_normalized, tropic_rsst_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

slopes_tropic_rsst_ch_pc2 = xr.apply_ufunc(linear_trend,
                          pc2_normalized, tropic_rsst_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )


def P__value(x, y):
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return p_value


pvalue_tropic_rsst_ch_pc1 = xr.apply_ufunc(P__value,
                          pc1_normalized, tropic_rsst_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )

pvalue_tropic_rsst_ch_pc2 = xr.apply_ufunc(P__value,
                          pc2_normalized, tropic_rsst_ch,
                          vectorize=True,
                          input_core_dims=[['sfc'], ['sfc']]
                         )


confidence_array_PC1 = pvalue_tropic_rsst_ch_pc1 <= 0.1
confidence_array_PC2 = pvalue_tropic_rsst_ch_pc2 <= 0.1


def plot(x, xname, level, cmap, confidence_array=None):
    lon1 = tropic_sst_ch["lon"]
    lat1 = tropic_sst_ch["lat"]
    lon2d, lat2d = np.meshgrid(lon1, lat1)
    xticks = ([0, 100, -160, -60])
    yticks = ([-20., 0, 20])
    fig = plt.figure(figsize=[6.5, 5])
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree(central_longitude=180), facecolor='white')
    plt.contourf(lon2d, lat2d, x, extend='both', levels=level,
                 transform=ccrs.PlateCarree(), cmap=cmap)
    ax.coastlines(color='white')
    plt.colorbar(location='bottom', pad=0.1, shrink=.9)
    plt.title(f'{xname}')
    land = cfeature.NaturalEarthFeature('physical', 'land', scale='110m',
                                        edgecolor='k', facecolor=cfeature.COLORS['land'])
    ax.add_feature(land, facecolor='white')
    if confidence_array is not None:
        stipple_mask = confidence_array > 0  # Use the boolean mask
        ax.scatter(lon2d[stipple_mask][::8], lat2d[stipple_mask][::8], 
                   s=.3, facecolors='none', edgecolors='dimgrey', marker='*',transform=ccrs.PlateCarree(), alpha=0.4, label='90% Confidence')
    ax.gridlines(draw_labels=True, xlocs=xticks, ylocs=yticks)
    plt.savefig(xname + '.eps', format='eps', dpi=500)

#RSST regression on IO PC1
name = 'regress tropics RSST vs PC1'
plot(slopes_tropic_rsst_ch_pc1, name, np.arange(-0.26, 0.28, 0.02), 'RdBu_r', confidence_array=confidence_array_PC1)

#RSST regression on IO PC2
name = 'regress tropics RSST vs PC2'
plot(slopes_tropic_rsst_ch_pc2, name, np.arange(-0.26, 0.28, 0.02), 'RdBu_r', confidence_array=confidence_array_PC2)




