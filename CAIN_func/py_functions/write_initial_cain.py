#================================================================
# AUTHORS: I. Drebot
# Write initial *.i file for CAIN
#================================================================

def write_initial_cain(stat_increase):
    import math
    import initial_param as p

    rnvar=2*stat_increase+3;

    angle=p.angle_deg*(math.pi/180); #initial scattered angle [rad]
    #print(p.NAME_FOR_OUTPUT_DIR + '/cain_tmp/initial.i')

    fp = open(p.NAME_FOR_GENERAL_OUTPUT_DIR + '/cain_tmp/initial_' + str(stat_increase) + '.i',  'w')
    fp.write (" ALLOCATE  MP=%d;\n" % (3*p.n_macro));
    fp.write (" \n");
    fp.write (" SET   photon=1, electron=2, positron=3, mm=1D-3, micron=1D-6, nm=1D-9, mu0=4*Pi*1D-7, \n");
    fp.write ("  psec=1e-12*Cvel,\n");
    fp.write (" \n");
    fp.write ("sigz=%f,\n" % p.bunch_length);
    fp.write ("ntcut=5,\n");
    fp.write ("laserwl=%f*nm, \n" % p.laserwl);
    fp.write ("pulseE=%f,\n" % p.pulseE);
    fp.write ("sigLrx=%f*micron,\n" % p.sigLrx);
    fp.write ("sigLry=%f*micron,\n" % p.sigLry);
    fp.write ("w0x=2*sigLrx,\n");
    fp.write ("w0y=2*sigLry,\n");
    fp.write ("raylx=Pi*w0x^2/laserwl, \n");
    fp.write ("rayly=Pi*w0y^2/laserwl, \n");
    fp.write ("sigt=%f*psec,\n" % p.sigt);
    fp.write ("angle=%f,  \n" % angle);
    fp.write ("tdl=1.0,\n");
    fp.write (" powerd=(2*pulseE*Cvel)/[Pi*sigt*Sqrt(2*Pi)*w0x*w0y],\n");

    if p.NPH>1:
        fp.write (" xi=(laserwl/(2*Pi*Emass))*Sqrt(powerd*mu0*Cvel),\n");
        Energy_eV=p.beam_energy_MeV*1e6
        fp.write (" ee= %f, !electron energy\n" % Energy_eV);
        fp.write (" lambda=(8*Pi*ee*Hbarc)/(laserwl*Emass^2),\n");

    fp.write (" \n");
    fp.write (" SET MsgLevel=1;\n");
    fp.write (" \n");
    fp.write (" SET Rand=5*%f;\n" % rnvar);
    fp.write (" \n");
    fp.write (" BEAM FILE='beam.txt';\n");
    fp.write (" \n");
    fp.write (" LASER LEFT, WAVEL=laserwl, POWERD=powerd,\n");
    fp.write (" \n");
    fp.write ("       TXYS=(%f, %f, %f, %f), \n" % (p.shifting_laser_t, p.shifting_laser_x, p.shifting_laser_y, p.shifting_laser_s));
    fp.write ("       E3=(-Sin(angle),0.0,-Cos(angle)), E1=(0,1,0),\n");
    fp.write ("       RAYLEIGH=(raylx,rayly), SIGT=sigt, GCUTT=ntcut, STOKES=(%f, %f, %f),\n" % (p.STOKES_1, p.STOKES_2, p.STOKES_3));
    fp.write ("       TDL=(tdl,tdl) ;\n");
    fp.write (" \n");
    fp.write (" \n");
    if p.NPH==0:
        fp.write (" LASERQED  COMPTON, NPH=0;\n");
    else:
        fp.write (" LASERQED  COMPTON, NPH=%2.0f, XIMAX=1.1*xi, LAMBDAMAX=5.1*lambda, PMAX=10 ;\n" % p.NPH);

    fp.write (" SET MsgLevel=0;  FLAG OFF ECHO;\n");
    fp.write (" SET Smesh=sigt/3;\n");
    # fp.write (" SET emax=1.001*ee, wmax=emax;\n");
    fp.write (" SET  it=0;\n");
    fp.write (" \n");
    fp.write (" PUSH  Time=(-ntcut*(sigt+sigz),ntcut*(sigt+sigz),%f);\n" % p.N_t_steps);
    fp.write ("       IF Mod(it,20)=0;\n");
    fp.write ("        PRINT it, FORMAT=(F6.0,'-th time step'); PRINT STAT, SHORT;\n");
    fp.write ("       ENDIF;\n");
    fp.write ("      SET it=it+1;\n");
    fp.write (" ENDPUSH;\n");
    fp.write (" \n");
    fp.write ("DRIFT T=0;\n"); # beam not take into account legth of interaction (like thin element L=0) Important when we use it different traking code to not change orbit length
    fp.write (" \n");
    fp.write ("WRITE BEAM, KIND=(electron), FILE='cain_output_electrons.dat';\n");
    fp.write (" \n");
    fp.write ("!PRINT STATISTICS, FILE='ELECRON_STAT.DAT';\n");
    fp.write (" \n");
    fp.write ("WRITE BEAM, KIND=(photon), FILE='cain_output_photons_%d.dat';\n" % stat_increase);
    fp.write (" \n");
    fp.write (" \n");
    fp.close()
