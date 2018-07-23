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
CCD_lens_transm = 0.8
CCD_aperture_r      = CCD_f/CCD_f_number/2
CCD_aperture_area   = CCD_aperture_r**2 * np.pi 
CCD_gain = 10

# integreal of (QE*spectrum)
CCD_efficiency  = 0.5
#collection angle
setup_omega     = CCD_aperture_area / setup_d**2
beam_area       = (1e-3)**2

n_emitted_photons   = 5e3
n_collected_photons = n_emitted_photons * np.cos(CCD_theta) * setup_omega * beam_area

n_counts = n_collected_photons * CCD_efficiency * CCD_lens_transm * CCD_gain