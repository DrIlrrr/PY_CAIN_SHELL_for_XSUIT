#================================================================
# AUTHORS: I. Drebot
# Shell for cain
#================================================================

import numpy as np
import initial_param as p
import sys
import os
import shutil
out_pwd=os.getcwd()
sys.path.append(out_pwd + '/CAIN_func/py_functions')
import call_cain 
import xsuit_2_cain_from_file
import cain_2_xsuit_from_file

# FCC param
turn_n=1
p.E_bunch=45600.*1e6
p.chargebunch=3.89329e-08
pass_to_csv='xsuit_beam/particle_dist_z_laserip.csv'
##

# Create output directory 
out_pwd=os.getcwd()+'/'+p.NAME_FOR_GENERAL_OUTPUT_DIR
# delete out directori if it is exist 
# protection to not use data from previus simulations
if os.path.isdir(out_pwd):
   shutil.rmtree(out_pwd)
os.mkdir(out_pwd)

# Main working directory for CAIN
CAIN_tmp_dir=out_pwd + "/cain_tmp";
os.mkdir(CAIN_tmp_dir)



#convert from xsuit to cain from the file
xsuit_2_cain_from_file.xsuit_2_cain_from_file(pass_to_csv)

# run CAIN Compton simulation
call_cain.call_cain(turn_n)

#convert from cain to xsuit 
cain_2_xsuit_from_file.cain_2_xsuit_from_file()




# clean from python cash files
os.popen('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
