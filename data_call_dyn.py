#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:53:21 2023

@author: gopika.s
"""


import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy as cart
"""open dataset"""


#dynamic variables loaded using the data_call_yr.py

"""Present day climatology computation """
clt_pr   = clt.sel(year=Present_period).mean("year")
huss_pr   = huss.sel(year=Present_period).mean("year")
sfcWind_pr   = sfcWind.sel(year=Present_period).mean("year")
hurs_pr   = hurs.sel(year=Present_period).mean("year")
tauu_pr   = tauu.sel(year=Present_period).mean("year")
tauv_pr   = tauv.sel(year=Present_period).mean("year")
zos_pr = zos.sel(year=Present_period).mean("year")
pr_pr = pr.sel(year=Present_period).mean("year")
tas_pr = tas.sel(year=Present_period).mean("year")
uas_pr = uas.sel(year=Present_period).mean("year")
vas_pr = vas.sel(year=Present_period).mean("year")

"""MMM of present day clim"""
CMIP_clt_pr_MMM = clt_pr.mean("sfc")
CMIP_huss_pr_MMM = huss_pr.mean("sfc")
CMIP_sfcWind_pr_MMM = sfcWind_pr.mean("sfc")
CMIP_hurs_pr_MMM = hurs_pr.mean("sfc")
CMIP_tauu_pr_MMM = tauu_pr.mean("sfc")
CMIP_tauv_pr_MMM  = tauv_pr.mean("sfc")
CMIP_zos_pr_MMM = zos_pr.mean("sfc")
CMIP_pr_pr_MMM = pr_pr.mean("sfc")
CMIP_tas_pr_MMM = tas_pr.mean("sfc")
CMIP_uas_pr_MMM = uas_pr.mean("sfc")
CMIP_vas_pr_MMM = vas_pr.mean("sfc")

"""Future climatology computation"""
clt_fu   = clt.sel(year=Future_period).mean("year")
huss_fu   = huss.sel(year=Future_period).mean("year")
sfcWind_fu   = sfcWind.sel(year=Future_period).mean("year")
hurs_fu   = hurs.sel(year=Future_period).mean("year")
tauu_fu   = tauu.sel(year=Future_period).mean("year")
tauv_fu   = tauv.sel(year=Future_period).mean("year")
zos_fu = zos.sel(year=Future_period).mean("year")
pr_fu = pr.sel(year=Future_period).mean("year")

tas_fu = tas.sel(year=Future_period).mean("year")
uas_fu = uas.sel(year=Future_period).mean("year")
vas_fu = vas.sel(year=Future_period).mean("year")


"""change"""

clt_ch   = clt_fu-clt_pr 
huss_ch   = huss_fu-huss_pr 
sfcWind_ch   = sfcWind_fu-sfcWind_pr 
hurs_ch   = hurs_fu-hurs_pr 
tauu_ch   = tauu_fu-tauu_pr 
tauv_ch   = tauv_fu-tauv_pr 
zos_ch = zos_fu-zos_pr 
pr_ch = pr_fu-pr_pr 

tas_ch = tas_fu-tas_pr 
uas_ch = uas_fu-uas_pr 
vas_ch = vas_fu-vas_pr 


"""MMM of Future-present change"""
CMIP_clt_change_MMM = clt_ch.mean("sfc")
CMIP_huss_change_MMM = huss_ch.mean("sfc")
CMIP_sfcWind_change_MMM = sfcWind_ch.mean("sfc")
CMIP_hurs_change_MMM = hurs_ch.mean("sfc")
CMIP_tauu_change_MMM = tauu_ch.mean("sfc")
CMIP_tauv_change_MMM  = tauv_ch.mean("sfc")
CMIP_zos_change_MMM = zos_ch.mean("sfc")
CMIP_pr_change_MMM = pr_ch.mean("sfc")

CMIP_tas_change_MMM = tas_ch.mean("sfc")
CMIP_uas_change_MMM = uas_ch.mean("sfc")
CMIP_vas_change_MMM = vas_ch.mean("sfc")
#CMIP_tropic_sst_change_MMM = tropic_sst_ch.mean("sfc")
#CMIP_tropic_rsst_change_MMM = tropic_rsst_ch.mean("sfc")


"""basin mean and the perturbations """
clt_ch_mean= clt_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
clt_ch_pert   = clt_ch - clt_ch_mean

huss_ch_mean= huss_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
huss_ch_pert   = huss_ch - huss_ch_mean

sfcWind_ch_mean= sfcWind_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
sfcWind_ch_pert   = sfcWind_ch - sfcWind_ch_mean

hurs_ch_mean= hurs_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
hurs_ch_pert   = hurs_ch - hurs_ch_mean

tauu_ch_mean= tauu_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
tauu_ch_pert   = tauu_ch - tauu_ch_mean

tauv_ch_mean= tauv_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
tauv_ch_pert   = tauv_ch - tauv_ch_mean

zos_ch_mean= zos_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
zos_ch_pert   = zos_ch - zos_ch_mean

pr_ch_mean= pr_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
pr_ch_pert   = pr_ch - pr_ch_mean

tas_ch_mean= tas_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
tas_ch_pert   = tas_ch - tas_ch_mean

uas_ch_mean= uas_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
uas_ch_pert   =uas_ch - uas_ch_mean

vas_ch_mean= vas_ch.mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
vas_ch_pert   = vas_ch - vas_ch_mean


""" MMM of the perturbations """
clt_ch_pert_MMM = clt_ch_pert.mean("sfc")
huss_ch_pert_MMM= huss_ch_pert.mean("sfc")
sfcWind_ch_pert_MMM=sfcWind_ch_pert.mean("sfc")
hurs_ch_pert_MMM=hurs_ch_pert.mean("sfc")
tauu_ch_pert_MMM=tauu_ch_pert.mean("sfc")
tauv_ch_pert_MMM=tauv_ch_pert.mean("sfc")
zos_ch_pert_MMM=zos_ch_pert.mean("sfc")
pr_ch_pert_MMM=pr_ch_pert.mean("sfc")
tas_ch_pert_MMM=tas_ch_pert.mean("sfc")
uas_ch_pert_MMM=uas_ch_pert.mean("sfc")
vas_ch_pert_MMM=vas_ch_pert.mean("sfc")















