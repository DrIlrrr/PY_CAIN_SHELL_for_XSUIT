#================================================================
# AUTHORS: I. Drebot
# Beam stat for electron beam (CAIN standart)
#================================================================
def beam_stat(file_name):
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    # file_name='beam.txt';

    el  = np.loadtxt(file_name);
    dir_for_safe = os.path.dirname(os.path.abspath(file_name))
    # file_name_0 = os.path.splitext(file_name)[0]
    # base=os.path.basename(file_name)
    file_name_0 = os.path.splitext(os.path.basename(file_name))[0]

    #dir_for_safe=file_name+'_stat'

    #os.mkdir(dir_for_safe)

    Echarge = 1.60e-19;# Charge of electron [c]
    #  0  1         2     3    4    5    6     7      8         9       10    11 12 13
    #  K GEN NAME Weight T(m) X(m) Y(m) S(m) E(eV) Px(eV/c) Py(eV/c) Ps(eV/c) Sx Sy Ss
    # matlab
    #  1  2         3     4    5    6    7     8      9        10       11    12 13 14

    weigth=np.max(el[:,2])

    x=el[:,4];
    y=el[:,5];
    s=el[:,3];

    E=el[:,7];

    px=el[:,8];
    py=el[:,9];
    pz=el[:,10];

    Sx=el[:,11];
    Sy=el[:,12];
    Sz=el[:,13];


    xp=px/pz;
    yp=py/pz;

    #geometrical emittace
    em_x=np.sqrt(np.mean((x-np.mean(x))**2)*np.mean((xp-np.mean(xp))**2)-np.mean((x-np.mean(x))*(xp-np.mean(xp)))**2);
    em_y=np.sqrt(np.mean((y-np.mean(y))**2)*np.mean((yp-np.mean(yp))**2)-np.mean((y-np.mean(y))*(yp-np.mean(yp)))**2);

    gamma=np.mean(E)/(0.511e6);
    delta_gamma=np.std(E/(0.511e6));
    norm_em_x=np.sqrt(gamma**2-1)*em_x;
    norm_em_y=np.sqrt(gamma**2-1)*em_y;

    energy_spread=np.std(E)/np.mean(E);


    fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(
        nrows=2, ncols=2,
        figsize=(10, 10)
    )
    # plt.grid(True)
    ax1.hist2d(x*1e6,xp, bins=30);
    #ax1.set_title('$\sigma_x$; $\sigma_y$')
    ax1.set_xlabel('$x\; [\mu m]$', size=20)
    ax1.set_ylabel('$x\'$', size=20)
    # ax1.grid(True)


    ax2.hist2d(y*1e6,yp, bins=30);
    ax2.set_xlabel('$y\;[\mu m]$', size=20)
    ax2.set_ylabel('$y\'$', size=20)
    # #ax2.set_title('$\epsilon_x$; $\epsilon_y$;')
    ax2.yaxis.tick_right()
    # ax2.grid(True)

    ax3.hist2d(x*1e6,y*1e6, bins=30);
    ax3.set_xlabel('$x\; [\mu m]$', size=20)
    ax3.set_ylabel('$y\;[\mu m]$', size=20)

    ax4.hist2d(s*1e3,E/1e6, bins=30);
    ax4.set_xlabel('$s\; [mm]$', size=20)
    ax4.set_ylabel('$E\; [MeV] $', size=20)
    ax4.yaxis.tick_right()
    # plt.show()
    fig.savefig(dir_for_safe + '/' + file_name_0 +'_stat.png')
    plt.close()
    #fig.savefig('foo.png')

    fp = open(dir_for_safe + '/' + file_name_0 +'_stat.txt', 'w')
    #fp = open('beam_stat.txt', 'w')
    fp.write ("-------------------------------------------------\n")
    fp.write ("N marco = %10.2e \n" % np.size(x))
    fp.write ("N particle = %10.5e\n" % (np.size(x)*weigth))
    fp.write ("Bunch charge = %10.5e [c]\n" % (np.size(x)*weigth*Echarge))
    fp.write ("-------------------------------------------------\n")
    fp.write ("mean_energy = %10.5e [MeV]\n" % np.mean(E))
    fp.write ("std_energy  = %10.5e [MeV]\n" % (np.std(E)/1e6) )
    fp.write ("energy_spread = %10.5e\n" % energy_spread)
    fp.write ("gamma = %10.5e\n" % gamma)
    fp.write ("delta_gamma = %10.5e\n" % delta_gamma)
    fp.write ("-------------------------------------------------\n")
    fp.write ("Electron beam non norm Emittances:\n")
    fp.write ("Emit X = %10.5e [m rad] \n" % em_x)
    fp.write ("Emit Y = %10.5e [m rad] \n" % em_y)
    fp.write ("Electron beam normalized Emittances:\n")
    fp.write ("Emit X n = %10.5e [m rad] \n" % norm_em_x);
    fp.write ("Emit Y n = %10.5e [m rad] \n" % norm_em_y);
    fp.write ("-------------------------------------------------\n")
    fp.write ("sigma_x = %10.5e [um]\n" % (np.std(x)*1e6));
    fp.write ("sigma_y = %10.5e [um]\n" % (np.std(y)*1e6));
    fp.write ("sigma_s = %10.5e [um]\n" % (np.std(s)*1e6));
    fp.write ("-------------------------------------------------\n")
    fp.close()
