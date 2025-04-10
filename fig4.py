    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gopika.s
"""
#Mean
dname2 = "Yearly"

execfile("data_call_yr.py")
execfile("zl_method.py")

execfile("diversity_mean_Computation/fig4_box_io.py")
execfile("diversity_mean_Computation/fig4_mean_comp_IO.py")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
SST_recon_mean = np.round(zh_T_mean_mmm.values,2)
contri_H_atm_mean =np.round(cont_H_atm_mean_MMM.values,2)
contri_Dyn_O_mean =np.round(cont_Dyn_O_mean_MMM.values,2)
contri_delta_lwd_a_mean =np.round(cont_delta_lwd_a_mean_MMM.values,2)
contri_delta_lhf_a_mean =np.round(cont_delta_lhf_a_mean_MMM.values,2)
contri_swr_mean =np.round(cont_rsntds_ch_mean_MMM.values,2)
contri_shf_mean =np.round(cont_hfss_ch_mean_MMM.values,2)
contri_residue_lwu_mean =np.round(cont_residue_lwu_mean_MMM.values,2)

width = .2
fig = plt.figure(figsize=(10, 3))
ax = fig.add_subplot(111)
xax=np.arange(0,9,1)
plt.ylim(-4,4)
xax = np.arange(9)
x_ticks_labels = [
    '', r'$\bar{SST}$',r'$\bar{Oce}$ ', r'$\bar{For}$ ', 
    r'$\bar{For_{lw}}$ ', r'$\bar{For_{lh}}$ ',
    r'$\bar{For_{sw}}$ ', r'$\bar{For_{sh}}$ '
]

plt.axhline(y=0, color='r', linestyle=':',alpha=.6)
#plt.axvline(x=3+.5,  color='gray', linestyle='-',alpha=.4)
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=11, fontfamily='serif')
ax.bar(xax[1], SST_recon_mean, width=width,  color='k', label='Annual')
ax.bar(xax[3], contri_H_atm_mean, width=width,  color='k')
ax.bar(xax[2], contri_Dyn_O_mean, width=width,  color='k')
ax.bar(xax[4], (contri_delta_lwd_a_mean+contri_residue_lwu_mean), width=width,  color='k')
ax.bar(xax[5], contri_delta_lhf_a_mean, width=width,  color='k')
ax.bar(xax[6], contri_swr_mean, width=width,  color='k')
ax.bar(xax[7], contri_shf_mean, width=width,  color='k')
ax.get_xticklabels()[1]
ax.get_xticklabels()[2]
ax.get_xticklabels()[3]
ax.get_xticklabels()[4]
ax.get_xticklabels()[5]
ax.get_xticklabels()[6]
ax.get_xticklabels()[7]
plt.legend(loc='lower right')
plt.title(f'IO Mean Contribution : Annual')
plt.savefig('fig-4a_mean.eps', format='eps', dpi=500)
plt.show()


#diversity

dname2 = "Yearly"
execfile("data_call_yr.py")
execfile("zl_method.py")
execfile("fig4_box_io.py")
execfile("fig4_diversity_IO.py")
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
var_T_calc_per=var_T_calc
cov_H_atm_star_per = cov_H_atm_star_per
cov_Dyn_O_star_per =cov_Dyn_O_star_per
cov_delta_lw_a_star_per =cov_delta_lw_a_star_per
cov_delta_lhf_a_star_per =cov_delta_lhf_a_star_per
cov_rsntds_star_per =cov_rsntds_star_per
cov_hfss_star_per =cov_hfss_star_per
cov_residue_lwu_star_per =cov_residue_lwu_star_per

width = 0.2
fig = plt.figure(figsize=(10, 3))
ax = fig.add_subplot(111)
xax=np.arange(0,9,1)
plt.ylim(-.75,.75)
xax = np.arange(9)
x_ticks_labels = [
    '', r'$\bar{SST}$', r'$\bar{Oce}$ ', r'$\bar{For}$ ',
    r'$\bar{For_{lw}}$ ', r'$\bar{For_{lh}}$ ',
    r'$\bar{For_{sw}}$ ', r'$\bar{For_{sh}}$ ', r'$\bar{lwu_r}$ '
]

plt.axhline(y=0, color='r', linestyle=':',alpha=.6)
plt.axvline(x=3+.5, color='gray', linestyle='-',alpha=.4)
ax.set_xticklabels(x_ticks_labels, rotation='horizontal', fontsize=11, fontfamily='serif')
ax.bar(xax[1], var_T_calc_per, width=width, color='k')
ax.bar(xax[3], cov_H_atm_star_per, width=width, color='k', label='Annual')
ax.bar(xax[2], cov_Dyn_O_star_per, width=width, color='k')
ax.bar(xax[4], cov_delta_lw_a_star_per, width=width, color='k')
ax.bar(xax[5], cov_delta_lhf_a_star_per, width=width, color='k')
ax.bar(xax[6], cov_rsntds_star_per, width=width, color='k')
ax.bar(xax[7], cov_hfss_star_per, width=width, color='k')
ax.get_xticklabels()[1]
ax.get_xticklabels()[2]
ax.get_xticklabels()[3]
ax.get_xticklabels()[4]
ax.get_xticklabels()[5]
ax.get_xticklabels()[6]
ax.get_xticklabels()[7]
plt.legend(loc='lower right')
plt.title(f'IO diversity Contribution : Annual')
plt.savefig('fig-4b_diversity.eps', format='eps', dpi=500)
plt.show()
    
