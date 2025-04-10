
######Diversity for perturbation
'each term GRAD mean and renaming'
zh_T_pert_pert_mean=zh_T_mean

cont_rsntds_ch_pert_mean=cont_rsntds_ch_mean
cont_delta_lwd_a_pert_mean =  cont_delta_lwd_a_mean
cont_delta_lhf_a_pert_mean = cont_delta_lhf_a_mean
cont_hfss_ch_pert_mean = cont_hfss_ch_mean
cont_residue_lwu_pert_mean = cont_residue_lwu_mean

cont_delta_Dyn_O_pert_mean =cont_Dyn_O_mean
cont_feedback_ocean_mean = np.nan
cont_H_atm_pert_mean = cont_rsntds_ch_pert_mean + cont_delta_lwd_a_pert_mean + cont_delta_lhf_a_pert_mean + cont_hfss_ch_pert_mean + cont_residue_lwu_pert_mean
