#================================================================
# AUTHORS: I. Drebot
# Convert beam from XSUIT format to CAIN standart
#================================================================

def xsuit_2_cain_from_file(pass_to_csv):

    import initial_param as p
    # import matplotlib.pyplot as plt
    import numpy as np
    import math as m


    chargebunch=p.chargebunch
    E_bunch=p.E_bunch

    beam_x = np.loadtxt(pass_to_csv, delimiter=',', skiprows=1)


    rest_mass = 0.511
    Echarge = 1.60e-19 # Charge of electron [c]

    X_COORDINATE=1
    Y_COORDINATE=2

    X_MOMENTUM=3
    Y_MOMENTUM=4

    delta_E=5
    S_COORDINATE=6


    n_macro=int(max(beam_x.shape))
    p.n_macro=n_macro

    X = beam_x[:,X_COORDINATE]
    Y = beam_x[:,Y_COORDINATE]
    Z = beam_x[:,S_COORDINATE]
    p.bunch_length=np.std(Z)

    Etot=E_bunch*(1+beam_x[:,delta_E])

    Ptot = np.sqrt(Etot**2 - rest_mass**2)

    Px = beam_x[:,X_MOMENTUM]*Ptot
    Py = beam_x[:,Y_MOMENTUM]*Ptot
    Pz = np.sqrt(Ptot**2 - Px**2 - Py**2)

    K0=2
    genname0 = 1


    Ne = chargebunch/Echarge # Number electrons in bunch
    weight0 = chargebunch/n_macro

    K = np.ones(n_macro)*K0 # 1 colomn
    genname = np.ones(n_macro)*genname0 # 2 colomn
    weight = np.ones(n_macro)*weight0 # 3 colomn
    # Creating polarizations
    Sx = np.zeros(n_macro)       # X polarizations
    Sy = np.zeros(n_macro)       # Y polarizations
    Ss = np.zeros(n_macro)       # s polarizations

    # CAIN_phasespace=[K, genname, weight, Z, X, Y, 0*Z, Etot, Px, Py, Pz, Sx, Sy, Ss]
    
    #  0  1         2     3    4    5    6     7      8         9       10    11 12 13
    #  K GEN NAME Weight T(m) X(m) Y(m) S(m) E(eV) Px(eV/c) Py(eV/c) Ps(eV/c) Sx Sy Ss
    # matlab
    #  1  2         3     4    5    6    7     8      9        10       11    12 13 14
    np.savetxt(p.NAME_FOR_GENERAL_OUTPUT_DIR + '/e_beam.txt', list(zip(K, genname, weight, 0*Z, X, Y, Z, Etot, Px, Py, Pz, Sx, Sy, Ss)), fmt=' %i    %i       %1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e % 1.12e ');

    import beam_stat
    beam_stat.beam_stat(p.NAME_FOR_GENERAL_OUTPUT_DIR + '/e_beam.txt')

    import shutil
    shutil.copy(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/' + '/e_beam.txt',p.NAME_FOR_GENERAL_OUTPUT_DIR + '/cain_tmp/beam.txt')