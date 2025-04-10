# Python-codes-for-Drivers-of-Future-Indian-Ocean-Warming-and-its-Spatial-Pattern-in-CMIP-Models-
Repository Overview – Figure Reproduction for Gopika et al. (2025)

This repository contains necessary Python scripts required to reproduce the figures presented in the Earth’s Future publication by Gopika et al. (2025), titled “Drivers of Future Indian Ocean Warming and its Spatial Pattern in CMIP Models.”

All analyses were conducted using Python.

Data Sources

The analysis relies on simulations from CMIP5 and CMIP6 climate model archives. All the required datasets can be accessed via:

    CMIP5:

        https://data.ceda.ac.uk/badc/cmip5/

        https://esgf-node.llnl.gov/search/cmip5/

    CMIP6:

        https://data.ceda.ac.uk/badc/cmip6/

        https://esgf-node.llnl.gov/projects/cmip6/

Preprocessing Instructions

Before executing any scripts, the downloaded CMIP data must be:

Converted to annual means, Spatially subset to the Indian Ocean domain, Restricted to the time period 1958–2087 and Combine all models into a single dataset (per variable) with an added coordinate named 'sfc', representing the model index or identifier

These preprocessing steps can be carried out using Climate Data Operators (CDO).

Script Descriptions

data_call_yr.py: Loads all the preprocessed CMIP datasets

zl_method.py: Computes SST, basin average, and RSST Future changes

data_call_dyn.py: processes dynamical variables 

An ad hoc mask, specifically created for this study, is also included in the repository.

Each figure-generating script automatically calls the required supporting modules. Before running any script, please ensure that all file paths are correctly configured to match your local directory structure.
