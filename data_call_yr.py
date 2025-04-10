
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy as cart
"""open dataset"""




###Preliminary analysis of the mechanism of the Indian Ocean (IO) warming paper.

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy as cart
"""open dataset"""
#The adhoc mask created loaded her but can apply earlier to the datas while processing
mask = xr.open_dataset("final_mask.nc")
mask1 = mask.mask1
"""components """
"The convention considers ocean gain as positive (+) and ocean loss as negative (-)"""
"""The signs have already been changed (from CMIP models) in the file being loaded for computation."""
"""Download all variables from CMIP5 and CMIP6 for all the selected models."""

'hfls= Surface upward latent heat w/m2' 'sign changed by *-1'
'hfss= Surface upward sensible heat w/m2' 'sign changed by *-1'
'rlds= Surface downwelling long wave radiation w/m2' 'sign same'
'rlus= Surface upwelling long wave radiation w/m2' 'sign changed by *-1'
'rsntds= Net downward shortwave radiation at sea water surface w/m2' 'sign same'
'sst= Sea Surface Temperature K' 'sign same'
'rsst= relative Sea Surface Temperature K' 'sign same'

#All the radiation data for all the model (variables listed above) for the Indian Ocean region, should be loaded here for the period from 1958 to 2088.
#The data for all models (a total of 47 models) are merged and arranged in a separate coordinate 'sfc' for ease of use
ds=xr.open_dataset("load CMIP simulations downloaded and processed for all radiation and for all models for IO region")

#The codes for calculating the lambda prime T, q, and effective height scale (lpt,lpq and lph terms) terms are already listed in SHAKESPEARE et al. (2022)
ds1=xr.open_dataset("load calculated lambda prime T, q, and effective height scale")

#Then load the dynamic variables listed below for understanding the mechanisms
do=xr.open_dataset("load CMIP simulations for all dynamic variables to understand the mechanism")
#CMIP models required for the following variables (some are optional) :
#clt   = Total cloud cover percentage unit in %
#huss   = Near surface specific humidity unit in g/kg instead of 1 (kg/kg)
#sfcWind   = Near surface wind speed unit in m/s
#hurs = Near surface relative humidity unit in m
#tauu   = Surface downward Eastward windstress unit in pa
#tauv   = Surface downward Northward windstress unit in pa
#zos = Sea surface height above geoid unit in m
#pr = Precipitation unit in m
#tas=Near surface air temperature 
#uas = Eastward wind unit in m/s
#vas = Northward wind unit in m/s


