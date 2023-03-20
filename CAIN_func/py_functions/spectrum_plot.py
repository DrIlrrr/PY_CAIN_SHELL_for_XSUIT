#================================================================
# AUTHORS: I. Drebot
# Plot specrums of scattered photons
#================================================================

def spectrum_plot():

        import matplotlib.pyplot as plt
        import numpy as np
        import math as m
        # import zipfile
        import initial_param as p
        import h5py

        # #load from zip
        # archive = zipfile.ZipFile(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/photons_beam.zip', 'r')
        # ph=np.loadtxt(archive.open('photons_data.txt'))

        # #load from txt
        # # ph  = np.loadtxt(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/photons_data.txt')
        # #ph  = np.loadtxt(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/cain_tmp/cain_output_photons_2.dat', skiprows=1)

        # #  0  1         2     3    4    5    6     7      8         9       10    11 12 13
        # #  K GEN NAME Weight T(m) X(m) Y(m) S(m) E(eV) Px(eV/c) Py(eV/c) Ps(eV/c) Sx Sy Ss
        # # matlab
        # #  1  2         3     4    5    6    7     8      9        10       11    12 13 14

        # x_phot=ph[:,4];
        # y_phot=ph[:,5];
        # z_phot=ph[:,6];
        # xp_phot=ph[:,8];
        # yp_phot=ph[:,9];
        # zp_phot=ph[:,10];
        # Sx=ph[:,11];
        # Sy=ph[:,12];
        # Sz=ph[:,13];

        # weigth=np.max(ph[:,2])

        # full_spectrum=ph[:,7]/1e3;

        #load from H5
        hf = h5py.File(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/data.h5', 'r')
        x_phot=np.array(hf.get('X_deviation'))
        y_phot=np.array(hf.get('Y_deviation'))
        z_phot=np.array(hf.get('Z_deviation'))
        xp_phot=np.array(hf.get('Pxi'))
        yp_phot=np.array(hf.get('Pyi'))
        zp_phot=np.array(hf.get('Pzi'))
        Sx=np.array(hf.get('Sx'))
        Sy=np.array(hf.get('Sy'))
        Sz=np.array(hf.get('Ss'))
        weigth=np.max(np.array(hf.get('weight0')))
        full_spectrum=np.array(hf.get('energy_deviation'))/1e3


        #import matplotlib.pyplot as plt
        spectrum=full_spectrum
        # An "interface" to matplotlib.axes.Axes.hist() method
        n, bins, patches = plt.hist(spectrum, bins=20,alpha=0.7, rwidth=0.9)#, color='#0504aa'
        plt.grid(True)#(axis='y', alpha=0.75)
        plt.xlabel('Photon energy [keV]')
        plt.ylabel('spectrum')
        plt.title('Total')
        #plt.text(15000, 3000, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        #plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        #plt.show()
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_2.png')
        plt.close()


        # import pandas as pd
        # commutes = pd.Series(spectrum)
        # commutes.plot.hist(grid=True, bins=20, rwidth=0.9,color='#607c8e')
        # plt.title('')
        # plt.xlabel('Photon energy [keV]')
        # plt.ylabel('spectrum')
        # plt.grid(axis='y', alpha=0.75)
        # plt.savefig('Sp_2.png')


        ## phot_angle

        phot_angle=np.sign(xp_phot)*np.arctan(np.sqrt(xp_phot**2+yp_phot**2)/zp_phot);

        n, bins, patches = plt.hist(phot_angle, bins=20,alpha=0.7, rwidth=0.9)#, color='#0504aa'
        plt.grid(True)
        # plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Theta')
        plt.ylabel('')
        plt.title('angular distribution')
        #plt.text(15000, 3000, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        #plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        #plt.show()
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_3.png')
        plt.close()


        theta=0.001;
        col=np.where(abs(phot_angle) < theta)

        plt.hist(np.squeeze(full_spectrum), bins=20,alpha=0.7, rwidth=0.9)#, color='#0504aa'
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Photon energy [keV]', size=16)
        # plt.ylabel('spectrum')
        plt.ylabel(r'$dN/dE$ [arbitrary units]', size=16)

        plt.title(r'$collimated\;in\;\theta$='+str(theta), size=16)
        maxfreq = n.max()
        # plt.show()
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_4.png')
        plt.close()

        ## with line
        theta=0.001;
        col=np.where(abs(phot_angle) < theta);
        sp_col=np.squeeze(full_spectrum[col]);
        N_eV=1000; #width of bin in eV
        nbin_plot=int(np.floor(max(sp_col)-min(sp_col))*(1000/N_eV));# nbin to make spectrum per KeV
        xs=np.linspace(min(sp_col),max(sp_col),num=int(nbin_plot));
        counts, bins = np.histogram(sp_col, bins=int(nbin_plot));
        plt.grid(True, alpha=0.75)
        plt.hist(bins[:-1], bins, weights=counts*weigth,alpha=0.7, rwidth=0.9)
        plt.plot(xs,counts*weigth)
        #n1, bins1, patches = plt.hist(sp_col, bins=int(nbin_plot),alpha=0.7, rwidth=0.9)#, color='#0504aa'
        # plt.hist(np.squeeze(ph[col,7]), bins=20,alpha=0.7, rwidth=0.9)#, color='#0504aa'
        plt.xlabel('Photon energy [keV]', size=16)
        plt.ylabel(r'$dN/dE$ per '+str(N_eV/1e3)+'$\;[keV]$', size=16)
        plt.title(r'$collimated\;in\;\theta$='+str(theta), size=16)
        maxfreq = n.max()
        # plt.show()
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_5.png')
        plt.close()
        np.savetxt(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_5.txt', list(zip(xs, counts*weigth)), fmt='%1.12e % 1.12e');




        ## Collimated mustage
        plt.hist2d(phot_angle[col],sp_col, bins=50);
        plt.xlabel('$\Theta$', size=16)
        plt.ylabel('Photon energy [keV]', size=16)
        # plt.show()
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_6.png')
        plt.close()


        ## Collimated mustage 2
        theta_mus=0.02;
        col_mus=np.where(abs(phot_angle) < theta_mus);
        sp_col_mus=np.squeeze(full_spectrum[col_mus]);

        plt.hist2d(phot_angle[col_mus],sp_col_mus, bins=100);
        plt.xlabel('$\Theta$', size=16)
        plt.ylabel('Photon energy [keV]', size=16)
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_7.png')
        plt.close()





        ## spot size at l=...[m]
        theta_gamma=0.04;
        col_gamma=np.where(abs(phot_angle) < theta_gamma);

        l=10;
        xcor_n_gamma=x_phot[col_gamma]+(xp_phot[col_gamma]/zp_phot[col_gamma])*l;
        ycor_n_gamma=y_phot[col_gamma]+(yp_phot[col_gamma]/zp_phot[col_gamma])*l;

        plt.hist2d(xcor_n_gamma,ycor_n_gamma, bins=30);
        plt.xlabel('x [m]', size=16)
        plt.ylabel('y [m]', size=16)
        plt.title(r'$spot\;size\;at\;L$='+str(l)+r'$\;[m]$', size=16)
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_8.png')
        plt.close()

        theta_mus=0.005; #limit of theta angle for mustage plot
        nbin=71;       # nbin for this plot must be line N+1 (101 71 51)
        col_mus=np.where(abs(phot_angle) < theta_mus);
        sp_col_mus=np.squeeze(full_spectrum[col_mus]);
        xedges = np.linspace(-theta_mus,theta_mus,int(nbin));
        # yedges = np.linspace(np.max(full_spectrum[np.where(phot_angle>theta_mus*6)]),np.max(full_spectrum),int(nbin));
        yedges = np.linspace(0,np.max(full_spectrum),int(nbin));
        #make data in 2d histogram
        h1, xedges1, yedges1 = np.histogram2d(phot_angle[col_mus],sp_col_mus, [xedges, yedges])
        #make integration on angle theta
        s=(nbin-1,nbin-1)
        nhis=np.zeros(s)
        h2=np.transpose(h1)
        # np.seterr(divide='ignore', invalid='ignore')
        for ni in range(0,nbin-1):
            nhis[:,ni]=h2[:,ni]/((np.pi/2)*(abs((xedges1[ni+1])**2-(xedges1[ni])**2)))


        #plot mustage
        # plt.pcolormesh(xedges1, yedges1, nhis, cmap='RdBu')



        plt.pcolormesh(xedges1*1e3, yedges1, nhis)
        plt.colorbar()
        plt.xlabel('$\Theta\;[mrad]$', size=16)
        plt.ylabel('Photon energy [keV]', size=16)
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_8.png')
        plt.close()



        #plot spot size
        theta_gamma=0.005;
        col_gamma=np.where(abs(phot_angle) < theta_gamma);
        ang=np.linspace(0,2*np.pi,50);
        r=l*np.tan(theta);
        xpt=r*np.cos(ang);
        ypt=r*np.sin(ang);
        l=8;
        xcor_n_gamma=x_phot[col_gamma]+(xp_phot[col_gamma]/zp_phot[col_gamma])*l;
        ycor_n_gamma=y_phot[col_gamma]+(yp_phot[col_gamma]/zp_phot[col_gamma])*l;
        h=plt.hist2d(xcor_n_gamma,ycor_n_gamma, bins=50);
        plt.plot(xpt,ypt,color='red');
        plt.xlabel('x [m]', size=16)
        plt.ylabel('y [m]', size=16)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(r'$spot\;size\;at\;L$='+str(l)+r'$\;[m]$', size=16)
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR +'/Sp_9.png')
        plt.close()
        np.savetxt(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_9.txt', h[0], fmt = "%s")


        #plot spot size
        col_gamma=np.where(abs(phot_angle) < theta);
        ang=np.linspace(0,2*np.pi,50);
        r=l*np.tan(theta);
        xpt=r*np.cos(ang);
        ypt=r*np.sin(ang);
        l=8;
        xcor_n_gamma=x_phot[col_gamma]+(xp_phot[col_gamma]/zp_phot[col_gamma])*l;
        ycor_n_gamma=y_phot[col_gamma]+(yp_phot[col_gamma]/zp_phot[col_gamma])*l;
        h=plt.hist2d(xcor_n_gamma,ycor_n_gamma, bins=50);
        plt.plot(xpt,ypt,color='red');
        plt.xlabel('x [m]', size=16)
        plt.ylabel('y [m]', size=16)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(r'$spot\;size\;at\;L$='+str(l)+r'$\;[m]$', size=16)
        plt.savefig(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR +'/Sp_10.png')
        plt.close()
        np.savetxt(p.NAME_FOR_GENERAL_OUTPUT_DIR+'/'+p.NAME_FOR_OUTPUT_DIR  + '/Sp_10.txt', h[0], fmt = "%s")
