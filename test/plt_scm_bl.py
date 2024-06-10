#!/usr/bin/env python

##############################################################################
#
# This script creates plots of the SCM RT baselines.
#
##############################################################################
import os
import sys
from rt_test_cases import run_list
from os.path import exists
import argparse
from plot_scm_out import plot_results

#
parser = argparse.ArgumentParser()
parser.add_argument('-drt', '--dir_bl', help='Directory containing SCM baselines', required=True)

#
def parse_args():
    args    = parser.parse_args()
    dir_bl  = args.dir_bl
    return (dir_bl)

#
def main():
    #
    (dir_bl) = parse_args()

    #
    error_count = 0
    for run in run_list:
        file_bl = dir_bl + "/" + run["case"]+"_"+run["suite"]+"/output.nc"
        if exists(file_bl):
            plot_files = plot_results(file_bl)

            # Setup output directories for plots.
            result = os.system("mkdir -p scm_bl_out/"+run["case"]+"/"+run["suite"])

            # Archive plots.
            com = "mv"
            for plot_file in plot_files:
                com = com + " " + plot_file
            # end for
            com = com + " scm_bl_out/" + run["case"] + "/" + run["suite"]
            result = os.system(com)
        # end if

    # Create tarball with plots.
    result = os.system('tar -cvf scm_bl_plots.tar scm_bl_out/*')

#
if __name__ == '__main__':
    main()
