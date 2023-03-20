#================================================================
# AUTHORS: I. Drebot
# Call cain
#================================================================
def call_cain(stat_increase):

    import os
    import initial_param as p
    import write_initial_cain

    write_initial_cain.write_initial_cain(stat_increase)

    working_dir_pwd=os.getcwd();
    DIRECTORY_FOR_CAIN=p.NAME_FOR_GENERAL_OUTPUT_DIR + "/cain_tmp"

    cain_home_dir=working_dir_pwd + "/CAIN_func/";

    os.system("cd " + DIRECTORY_FOR_CAIN + "; " + cain_home_dir + "cain_compiled.mac < initial_" + str(stat_increase) + ".i > cain_out.txt"); # start cain


    if stat_increase>1:
            os.remove(DIRECTORY_FOR_CAIN+ '/initial_' + str(stat_increase) + '.i')




#else
    # os.system("cd " + DIRECTORY_FOR_CAIN + "; " + cain_home_dir + "cain.ub_illya/cain240/src/cain.exe < initial.i > cain_out.txt"); # start cain
    # os.system(['cd ' DIRECTORY_FOR_CAIN '; ' home_dir 'cain.ub_illya/cain240/src/cain.exe < newbeam_tmp.i > cain.out']); # start cain
#end


