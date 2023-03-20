#================================================================
# AUTHORS: I. Drebot
# Initial parameters for CAIN
#================================================================

NAME_FOR_GENERAL_OUTPUT_DIR='output';

### LASER parameteres
angle_deg=0;               # in degree
pulseE=0.000001;           #laser puse energy [J]
sigLrx=1000;                 #/2; % given in [mu m] micro meter like 2 weist w0=28;
sigLry=1000;                 #/2; % given in [mu m] micro meter like 2 weist w0=28;
laserwl=800;                # laser wavelenth [nm] nano meters
sigt=300;                    #pulse length [ps]
shifting_laser_x = 0;  #
shifting_laser_y = 0;  #
shifting_laser_s = 0;  #
shifting_laser_t = 0;  #shifting_laser_t;  %

NPH=0; #is Maximum number of laser photons to be absorbed in one process NPH=0 linear, NPH>= 1, use nonlinear formula.

N_t_steps=250; #Number of time steps for linear can be 250-300 for non-linear bigger

#STOKES:  linear [0 0 1]; circular [0 1 0]
STOKES_1=0;
STOKES_2=0;
STOKES_3=1;
