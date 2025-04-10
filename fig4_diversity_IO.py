#Terms from fig4_box_io.py
######Diversity for perturbation

#Your equation for one model is T= F1 + F2 + F3   (F1,2,3 are the various terms that contribute to the diversity)

cont_zh_T_mean_pert_recal = (cont_rsntds_ch_pert_mean + cont_delta_lwd_a_pert_mean + cont_delta_lhf_a_pert_mean + 
                        cont_hfss_ch_pert_mean + cont_residue_lwu_pert_mean + cont_delta_Dyn_O_pert_mean+cont_feedback_ocean_mean)  
cont_delta_lw_a_pert_mean= cont_delta_lwd_a_pert_mean+cont_residue_lwu_pert_mean

# MMM of each term
zh_T_pert_pert_mean_MMM = zh_T_pert_pert_mean.mean("sfc")
cont_rsntds_ch_pert_mean_MMM = cont_rsntds_ch_pert_mean.mean("sfc")
cont_delta_lwd_a_pert_mean_MMM = cont_delta_lwd_a_pert_mean.mean("sfc")
cont_delta_lw_a_pert_mean_MMM = cont_delta_lw_a_pert_mean.mean("sfc")

cont_delta_lhf_a_pert_mean_MMM = cont_delta_lhf_a_pert_mean.mean("sfc")
cont_hfss_ch_pert_mean_MMM = cont_hfss_ch_pert_mean.mean("sfc")
cont_residue_lwu_pert_mean_MMM = cont_residue_lwu_pert_mean.mean("sfc")
cont_delta_Dyn_O_pert_mean_MMM =cont_delta_Dyn_O_pert_mean.mean("sfc")

#Subtract the MMM values from each model to get: T*= F1* + F2* + F3*
rsntds_star = cont_rsntds_ch_pert_mean-cont_rsntds_ch_pert_mean_MMM
delta_lwd_a_star = cont_delta_lwd_a_pert_mean-cont_delta_lwd_a_pert_mean_MMM
delta_lw_a_star = cont_delta_lw_a_pert_mean-cont_delta_lw_a_pert_mean_MMM

delta_lhf_a_star = cont_delta_lhf_a_pert_mean-cont_delta_lhf_a_pert_mean_MMM
hfss_star = cont_hfss_ch_pert_mean-cont_hfss_ch_pert_mean_MMM
residue_lwu_star=cont_residue_lwu_pert_mean-cont_residue_lwu_pert_mean_MMM
Dyn_O_star=cont_delta_Dyn_O_pert_mean-cont_delta_Dyn_O_pert_mean_MMM

#calculation T*

T_bar_star= zh_T_pert_pert_mean-zh_T_pert_pert_mean_MMM

#Multiply each model equation by T* to get T*^2 = F1*T* + F2*T* + F3*T*

T_bar_star_sqr= T_bar_star * T_bar_star

rsntds_star_sqr = rsntds_star * T_bar_star
delta_lwd_a_star_sqr = delta_lwd_a_star * T_bar_star
delta_lw_a_star_sqr = delta_lw_a_star * T_bar_star

delta_lhf_a_star_sqr = delta_lhf_a_star * T_bar_star
hfss_star_sqr = hfss_star * T_bar_star
residue_lwu_star_sqr = residue_lwu_star * T_bar_star
Dyn_O_star_sqr = Dyn_O_star * T_bar_star

#Sum over the N models and divide by N-1 to get C(T) =coC( F1,T) + coC(F2,T) + coC(F3,T)
N = 46

cov_rsntds_star = rsntds_star_sqr.sum("sfc")/(N-1)
cov_delta_lwd_a_star = delta_lwd_a_star_sqr.sum("sfc")/(N-1)
cov_delta_lw_a_star = delta_lw_a_star_sqr.sum("sfc")/(N-1)

cov_delta_lhf_a_star = delta_lhf_a_star_sqr.sum("sfc")/(N-1)
cov_hfss_star = hfss_star_sqr.sum("sfc")/(N-1)
cov_residue_lwu_star = residue_lwu_star_sqr.sum("sfc")/(N-1)
cov_Dyn_O_star = Dyn_O_star_sqr.sum("sfc")/(N-1)

cov_H_atm_star =cov_rsntds_star+ cov_delta_lw_a_star + cov_delta_lhf_a_star + cov_hfss_star


var_T_calc=(cov_rsntds_star+cov_delta_lw_a_star+cov_delta_lhf_a_star+cov_hfss_star
            +cov_Dyn_O_star)




# covariance 
variance_T_calc_per = (var_T_calc)

cov_rsntds_star_per = (cov_rsntds_star)
cov_delta_lwd_a_star_per = (cov_delta_lwd_a_star)
cov_delta_lw_a_star_per = (cov_delta_lw_a_star)

cov_delta_lhf_a_star_per = (cov_delta_lhf_a_star)
cov_hfss_star_per = (cov_hfss_star)
cov_residue_lwu_star_per = (cov_residue_lwu_star)
cov_Dyn_O_star_per = (cov_Dyn_O_star)

cov_H_atm_star_per = (cov_rsntds_star_per + cov_delta_lw_a_star_per + 
                      cov_delta_lhf_a_star_per+cov_hfss_star_per)


