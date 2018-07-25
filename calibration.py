# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

setup_d     = 700e-3

CCD_theta       = np.pi/6
CCD_f_number    = 2
CCD_f           = 16e-3
CCD_lens_transm = 0.9
CCD_aperture_r      = CCD_f/CCD_f_number/2
CCD_aperture_area   = CCD_aperture_r**2 * np.pi 
CCD_gain = 1

# integreal of (QE*spectrum)
CCD_efficiency  = 0.53
#collection angle
setup_omega     = CCD_aperture_area / setup_d**2
beam_area       = (1e-3)**2

n_emitted_photons   = 5.6e3
n_collected_photons = n_emitted_photons * np.cos(CCD_theta) * setup_omega 
#* beam_area

charge_elec_pC = 1.602e-7

n_counts = 1e8
n_elec = n_counts / (n_collected_photons * CCD_efficiency * CCD_lens_transm * CCD_gain) 

charge = n_elec * charge_elec_pC

print(charge)