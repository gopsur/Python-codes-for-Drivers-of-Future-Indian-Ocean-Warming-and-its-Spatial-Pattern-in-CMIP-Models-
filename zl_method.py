
"""

@author: gopika.s
"""
#dall the variables loaded using the data_call_yr.py

"""variables"""
hfls   = ds.hfls.sel(lat=slice(-20.5,30.5)) 
hfss   = ds.hfss.sel(lat=slice(-20.5,30.5)) 
rlds   = ds.rlds.sel(lat=slice(-20.5,30.5)) 
rlus   = ds.rlus.sel(lat=slice(-20.5,30.5)) 
rsntds = ds.rsntds.sel(lat=slice(-20.5,30.5)) 
sst    = ds.sst.sel(lat=slice(-20.5,30.5)) 

"""Periods for defining present-day and future state."""
Present_period =  slice(1958,1977)
Future_period  =  slice(2068,2087)

"""Present-day climatology"""
hfls_pr   = hfls.sel(year=Present_period).mean("year")
hfss_pr   = hfss.sel(year=Present_period).mean("year")
rlds_pr   = rlds.sel(year=Present_period).mean("year")
rlus_pr   = rlus.sel(year=Present_period).mean("year")
rsntds_pr = rsntds.sel(year=Present_period).mean("year")
sst_pr    = sst.sel(year=Present_period).mean("year")

"""Future climatology"""
hfls_fu   = hfls.sel(year=Future_period).mean("year")
hfss_fu   = hfss.sel(year=Future_period).mean("year")
rlds_fu   = rlds.sel(year=Future_period).mean("year")
rlus_fu   = rlus.sel(year=Future_period).mean("year")
rsntds_fu = rsntds.sel(year=Future_period).mean("year")
sst_fu    = sst.sel(year=Future_period).mean("year")

"""future change"""

hfds_ch   = hfds_fu-hfds_pr 
hfls_ch   = hfls_fu-hfls_pr 
hfss_ch   = hfss_fu-hfss_pr 
rlds_ch   = rlds_fu-rlds_pr 
rlus_ch   = rlus_fu-rlus_pr 
rsntds_ch = rsntds_fu-rsntds_pr 
sst_ch    = sst_fu-sst_pr 


"""SST change reconstruction equation"""


#direct components needed from cmip to compute zhang and li
delta_Qsw  = rsntds_ch
delta_Qshf = hfss_ch

'delta_D0 = - Delta_Qnet ; so here we are combining the components of Qnet.'
delta_D0    = - (rsntds_ch + rlds_ch + rlus_ch + hfls_ch + hfss_ch)

"""Calculation of longwave downward radiation: ocean and atmospheric parts."""
'Longwave downward part: water vapor feedback exceeds direct radiative forcing, so we follow the method of SHAKESPEARE et al. to separate out the longwave downward feedback.'
tot_lwd_feed= lpt + lpq + lph

delta_lwd_o = (tot_lwd_feed) * sst_ch

delta_lwd_a = rlds_ch - delta_lwd_o

"""Calculation of longwave upward radiation: ocean and atmospheric parts."""
'Longwave upward part: ocean-dependent, so we are not taking rlus data from CMIP models; 4 sigma cube (present SST climatology) SST change.'
sigma = 5.67 * 10**-8 # w/(m2K4)

delta_lw_up = -1* 4 * sigma * (sst_pr**3) * sst_ch

residue_lwu = rlus_ch - delta_lw_up
"""Calculation of LHF: ocean and atmospheric parts."""
'LHF has atmospheric and ocean components. The ocean part is calculated as γ1×present day Qlh×SST change; where γ1​ for the tropics is 0.06 as per Zhang and Li.'


delta_lhf_o = 0.06 * hfls_pr * sst_ch

delta_lhf_a = hfls_ch - delta_lhf_o

"""Calculation of ocean coefficients."""
'Ocean coefficient = coefficient of longwave upward + coefficient of latent heat flux (LHF) ocean part + total longwave downward feedback.'

"""feedbacks"""
lwup_feed = 4 * sigma * (sst_pr**3)
lhf_feed = 0.06 * (-1*  hfls_pr) #feed back coeff is positive so, changing the sign back (sign considered negative as lhf is a loss)
"lw up and latend heat flux are  feedback coeffs positive, while lwd feedback coeff is negative"
ocean_coeff = lwup_feed + lhf_feed - tot_lwd_feed
alpha= ocean_coeff

'The new updated SST future change equation'

H_atm = delta_Qsw + delta_lwd_a + delta_lhf_a + delta_Qshf + residue_lwu
Dyn_O = delta_D0

delta_ts =  (H_atm + Dyn_O) / alpha

'each term contribution'

cont_delta_Hatm = H_atm / alpha
cont_delta_Dyn_O = Dyn_O / alpha


cont_delta_Qsw = delta_Qsw / alpha
cont_delta_lwd_a = delta_lwd_a / alpha 
cont_delta_lhf_a = delta_lhf_a / alpha
cont_residue_lwu = residue_lwu / alpha
cont_delta_Qshf = delta_Qshf / alpha
cont_delta_D0 = delta_D0 / alpha

"""MMM feedbacks"""
alpha_MMM = alpha.mean("sfc")
lwup_feed_MMM = lwup_feed.mean("sfc")
lhf_feed_MMM = lhf_feed.mean("sfc")
tot_lwd_feed_MMM = (tot_lwd_feed*-1).mean("sfc")


"""MMM of each terms """
CMIP_SST_change_MMM = sst_ch.mean("sfc")
delta_ts_MMM = delta_ts.mean("sfc")
H_atm_MMM = H_atm.mean("sfc")
Dyn_O_MMM = Dyn_O.mean("sfc")
cont_delta_Qsw_MMM  = cont_delta_Qsw.mean("sfc")
cont_delta_lwd_a_MMM = cont_delta_lwd_a.mean("sfc")
cont_delta_lhf_a_MMM= cont_delta_lhf_a.mean("sfc")
cont_residue_lwu_MMM= cont_residue_lwu.mean("sfc")
cont_delta_Qshf_MMM = cont_delta_Qshf.mean("sfc")
cont_delta_D0_MMM   = cont_delta_D0.mean("sfc")
cont_delta_Hatm_MMM = cont_delta_Hatm.mean("sfc")
cont_delta_Dyn_O_MMM= cont_delta_Dyn_O.mean("sfc")


"""For RSST and mean part of the equations"""
###########################
""""""""""""
"""Relative part""" 
sst_ch_mean= sst_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rsst_ch_pert   = sst_ch - sst_ch_mean

hfls_ch_mean= hfls_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rhfls_ch_pert  = hfls_ch - hfls_ch_mean

hfss_ch_mean= hfss_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rhfss_ch_pert   = hfss_ch - hfss_ch_mean

rlds_ch_mean= rlds_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rrlds_ch_pert   = rlds_ch - rlds_ch_mean

rlus_ch_mean= rlus_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rrlus_ch_pert   = rlus_ch - rlus_ch_mean

rsntds_ch_mean= rsntds_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
rrsntds_ch_pert   = rsntds_ch - rsntds_ch_mean

'calculation: relative lhf ocean and atmospheric part'

delta_lhf_o_mean = delta_lhf_o.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
delta_lhf_a_mean = delta_lhf_a.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

rdelta_lhf_o_pert = delta_lhf_o - delta_lhf_o_mean
rdelta_lhf_a_pert = delta_lhf_a - delta_lhf_a_mean

'calculation: relative lwd ocean and atmospheric part'

delta_lwd_o_mean = delta_lwd_o.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
delta_lwd_a_mean = delta_lwd_a.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

rdelta_lwd_o_pert = delta_lwd_o - delta_lwd_o_mean
rdelta_lwd_a_pert = delta_lwd_a - delta_lwd_a_mean

'calculation: relative residue lwup ocean and atmospheric part'
delta_lw_up_mean = delta_lw_up.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

residue_lwu_mean = residue_lwu.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

residue_lwu_pert = residue_lwu - residue_lwu_mean

'Relative Dynamic Ocean'
Dyn_Oce_mean    = - (rsntds_ch_mean + rlds_ch_mean + rlus_ch_mean + hfls_ch_mean + hfss_ch_mean)
Dyn_Oce_pert    = - (rrsntds_ch_pert + rrlds_ch_pert + rrlus_ch_pert + rhfls_ch_pert + rhfss_ch_pert)


'Relative H-atmosphere'

H_atm_mean = rsntds_ch_mean + delta_lwd_a_mean + delta_lhf_a_mean + hfss_ch_mean + residue_lwu_mean
H_atm_per = rrsntds_ch_pert + rdelta_lwd_a_pert + rdelta_lhf_a_pert + rhfss_ch_pert + residue_lwu_pert


'Relative alpha'

alpha_mean = alpha.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
alpha_pert = alpha - alpha_mean
alpha_pert_MMM= alpha_pert.mean("sfc")
alpha_star = alpha_pert/alpha_mean
alpha_mean_MMM= alpha_mean.mean("sfc")


"""T Means and Relative T"""

#For basin average
zh_T_mean = (H_atm_mean + Dyn_Oce_mean) / alpha_mean_MMM
feedback_ocean = -(zh_T_mean*alpha_pert)
##For RSST, feedback ocean is already accounted negative
zh_T_pert = (H_atm_per+Dyn_Oce_pert+feedback_ocean)/alpha_mean_MMM

##################################################
##For further calculations
'each mean term contribution =>divided by alpha_mean'
cont_rsntds_ch_mean = rsntds_ch_mean / alpha_mean_MMM
cont_delta_lwd_a_mean = delta_lwd_a_mean / alpha_mean_MMM 
cont_delta_lhf_a_mean = delta_lhf_a_mean / alpha_mean_MMM
cont_hfss_ch_mean = hfss_ch_mean / alpha_mean_MMM
cont_residue_lwu_mean = residue_lwu_mean / alpha_mean_MMM
cont_Dyn_Oce_mean = Dyn_Oce_mean / alpha_mean_MMM
cont_H_atm_mean = cont_rsntds_ch_mean + cont_delta_lwd_a_mean + cont_delta_lhf_a_mean + cont_hfss_ch_mean + cont_residue_lwu_mean
cont_Dyn_O_mean = cont_Dyn_Oce_mean

'MMM of mean terms contribution'
Dyn_Oce_mean_MMM = Dyn_Oce_mean.mean("sfc")
alpha_mean_MMM= alpha_mean.mean("sfc")
H_atm_mean_MMM = H_atm_mean.mean("sfc")
sst_ch_mean_MMM = sst_ch_mean.mean("sfc")
cont_rsntds_ch_mean_MMM  = cont_rsntds_ch_mean.mean("sfc")
cont_delta_lwd_a_mean_MMM    = cont_delta_lwd_a_mean.mean("sfc")
cont_delta_lhf_a_mean_MMM= cont_delta_lhf_a_mean.mean("sfc")
cont_hfss_ch_mean_MMM    = cont_hfss_ch_mean.mean("sfc")
cont_residue_lwu_mean_MMM    = cont_residue_lwu_mean.mean("sfc")
cont_Dyn_O_mean_MMM    = cont_Dyn_Oce_mean.mean("sfc")
cont_H_atm_mean_MMM = cont_H_atm_mean.mean("sfc")
zh_T_mean_mmm = zh_T_mean.mean("sfc")

'each perturbation term contribution =>divided by alpha' 
rsst_ch_pert_MMM = rsst_ch_pert.mean("sfc")
zh_T_pert_MMM    = zh_T_pert.mean("sfc")
cont_delta_Hatm_pert = (H_atm_per/alpha_mean_MMM) 
cont_delta_Dyn_O_pert= (Dyn_Oce_pert/alpha_mean_MMM) 
cont_rsntds_ch_pert =  (rrsntds_ch_pert / alpha_mean_MMM) 
cont_delta_lwd_a_pert = (rdelta_lwd_a_pert / alpha_mean_MMM)
cont_delta_lhf_a_pert = (rdelta_lhf_a_pert / alpha_mean_MMM)
cont_residue_lwu_pert = (residue_lwu_pert / alpha_mean_MMM)
cont_hfss_ch_pert = (rhfss_ch_pert / alpha_mean_MMM)
cont_feedback_ocean= (feedback_ocean / alpha_mean_MMM)

'MMM of perturbation terms contribution'
zh_T_pert_mmm = zh_T_pert.mean("sfc")
cont_delta_Hatm_pert_MMM = cont_delta_Hatm_pert.mean("sfc")
cont_delta_Dyn_O_pert_MMM = cont_delta_Dyn_O_pert.mean("sfc")
cont_feedback_ocean_MMM = cont_feedback_ocean.mean("sfc")
cont_rsntds_ch_pert_MMM  = cont_rsntds_ch_pert.mean("sfc")
cont_delta_lwd_a_pert_MMM    = cont_delta_lwd_a_pert.mean("sfc")
cont_delta_lhf_a_pert_MMM= cont_delta_lhf_a_pert.mean("sfc")
cont_residue_lwu_pert_MMM= residue_lwu_pert.mean("sfc")
cont_hfss_ch_pert_MMM    = cont_hfss_ch_pert.mean("sfc")








