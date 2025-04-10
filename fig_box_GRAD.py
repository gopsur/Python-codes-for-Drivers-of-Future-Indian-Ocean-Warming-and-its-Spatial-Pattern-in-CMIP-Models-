
######Diversity for perturbation
'each perturbation term gradient (applicable for ZGRAD and MGRAD) mean'
zh_T_pert_pert_mean=zh_T_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-zh_T_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

cont_rsntds_ch_pert_mean=cont_rsntds_ch_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True) - cont_rsntds_ch_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
cont_delta_lwd_a_pert_mean =  cont_delta_lwd_a_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)- cont_delta_lwd_a_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
cont_delta_lhf_a_pert_mean = cont_delta_lhf_a_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)- cont_delta_lhf_a_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
cont_hfss_ch_pert_mean = cont_hfss_ch_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)- cont_hfss_ch_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
cont_residue_lwu_pert_mean = cont_residue_lwu_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-cont_residue_lwu_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

cont_delta_Dyn_O_pert_mean = cont_delta_Dyn_O_pert.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-cont_delta_Dyn_O_pert.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)
cont_feedback_ocean_mean =cont_feedback_ocean.sel(lon=lon1,lat=lat1).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)-cont_feedback_ocean.sel(lon=lon2,lat=lat2).mean(dim=["lon", "lat"],skipna=True,keep_attrs=True)

cont_H_atm_pert_mean = cont_rsntds_ch_pert_mean + cont_delta_lwd_a_pert_mean + cont_delta_lhf_a_pert_mean + cont_hfss_ch_pert_mean + cont_residue_lwu_pert_mean
