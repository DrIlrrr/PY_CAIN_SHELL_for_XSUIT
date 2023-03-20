#================================================================
# AUTHORS: I. Drebot
# Convert beam from CAIN format to XSUIT standart
#================================================================

def cain_2_xsuit_from_file():

    import os
    import numpy as np
    import initial_param as p
    import shutil
    import pandas as pd
    # define function to replace "D" by "e" in DAT file
    # from FORTRAN notation to PYTHON
    def replace_d_exp(s):
        return s.replace(b'D', b'e')

    out_pwd=os.getcwd()

    beam = np.loadtxt(out_pwd + "/" + p.NAME_FOR_GENERAL_OUTPUT_DIR + '/cain_tmp/cain_output_electrons.dat', skiprows=1, converters={n: replace_d_exp for n in range(14)})
    
    E_bunch=p.E_bunch

    #  0  1         2     3    4    5    6     7      8         9       10    11 12 13
    #  K GEN NAME Weight T(m) X(m) Y(m) S(m) E(eV) Px(eV/c) Py(eV/c) Ps(eV/c) Sx Sy Ss
    # matlab
    #  1  2         3     4    5    6    7     8      9        10       11    12 13 14


    x=beam[:,4]
    y=beam[:,5]

    zeta=beam[:,6]
    Etot=beam[:,7]

    # Etot=E_bunch.*(1+delta_E);

    delta_E=(Etot-E_bunch)/E_bunch

    rest_mass = 0.511

    Ptot = np.sqrt(Etot**2 - rest_mass**2)

    px = beam[:,8]/Ptot
    py = beam[:,9]/Ptot
    # Pz = sqrt(Ptot**2 - Px**2 - Py**2)

    # first_colon=[1:1:length(x)]

    beam_xsuit={'x': x, 'y': y, 'px': px, 'py': py, 'delta': delta_E, 'zeta':zeta}
    T = pd.DataFrame(beam_xsuit)
    T.to_csv(f"{p.NAME_FOR_GENERAL_OUTPUT_DIR}/electrons_after_compton.csv")

    