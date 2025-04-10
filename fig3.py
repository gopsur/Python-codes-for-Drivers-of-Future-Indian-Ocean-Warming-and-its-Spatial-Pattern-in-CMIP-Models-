    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: gopika.s
"""
from scipy import stats
dname2 = "Yearly"

execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("data_call_dyn.py")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import seaborn as sns



def scatter(xl, yl, x, y, xlab, ylab, reg, savename):
   fig, ax = plt.subplots(figsize=(8, 6))
   plt.ylim(yl)  # Set y-axis limits
   plt.xlim(xl)  # Set x-axis limits

   # Scatter plot of the data points
   ax.scatter(x, y, c='dimgray', marker='o', s=30, label='Data Points')

   # Regression plots
   sns.regplot(x=x, y=y, scatter=False, color='green', ci=95, ax=ax)
   sns.regplot(x=x, y=y, scatter=False, color='black', ci=0, ax=ax)

   # Labels and title
   ax.set_xlabel(xlab, fontsize=14)
   ax.set_ylabel(ylab, fontsize=14)
   ax.set_title(f'{xlab} vs. {ylab} for {reg}', fontsize=16)

   # Grid
   ax.grid(True, linestyle='--', alpha=0.6)

   # Add correlation coefficient and slope
   corr_coefficient = np.corrcoef(x, y)[0, 1]
   ax.text(xl[0] + 0.05, yl[1] - 0.2, f'R: {corr_coefficient:.2f}', fontsize=14, fontweight='bold', color='r')

   slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
   ax.text(xl[0] + 0.05, yl[1] - 0.4, f'Slope: {slope:.2f}', fontsize=14, fontweight='bold', color='b')

   print(f"Slope: {slope}, Intercept: {intercept}, R: {r_value}, P: {p_value}, Std Err: {std_err}")

   # Add mean point
   x_mean = x.mean()
   y_mean = y.mean()
   ax.scatter(x_mean, y_mean, c='red', marker='*', s=100, label='Mean Point')

   # Vertical and horizontal reference lines
   plt.axhline(y=0, color='orange', linestyle=':')
   plt.axvline(x=0, color='orange', linestyle=':')

   # Save the figure
   plt.savefig(f'fig_{savename}_{reg}.eps', format='eps', dpi=500)

   plt.show()



#ZGRAD
#EIO
lon1=slice(85,105);lat1=slice(-13,3)
#SIO
lon2=slice(40,65);lat2=slice(-10,15)

rsst_ch_pert_ew=rsst_ch_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-rsst_ch_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
zh_T_pert_ew=zh_T_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-zh_T_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
scatter((-1.2,1.2),(-1.2,1.2),rsst_ch_pert_ew.values,zh_T_pert_ew.values,'Simulated RSST','Reconstructed RSST','ZGRAD_mean','simu_RSST_vs_recon_RSST')

#MGRAD
#NH 
lon3=slice(40,105);lat3=slice(0,25)
#SH
lon4=slice(40,105);lat4=slice(-20,-10)

rsst_ch_pert_ns=rsst_ch_pert.sel(lon=lon3,lat=lat3).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-rsst_ch_pert.sel(lon=lon4,lat=lat4).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
zh_T_pert_ns=zh_T_pert.sel(lon=lon3,lat=lat3).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-zh_T_pert.sel(lon=lon4,lat=lat4).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
scatter((-1.2,1.2),(-1.2,1.2),rsst_ch_pert_ns.values,zh_T_pert_ns.values,'Simulated RSST','Reconstructed RSST','MGRAD_mean','simu_RSST_vs_recon_RSST')

#IO average
scatter((1,5),(1,5),sst_ch_mean.values,zh_T_mean.values,'Simulated RSST','Reconstructed SST','IO_mean','simu_RSST_vs_recon_SST')






























