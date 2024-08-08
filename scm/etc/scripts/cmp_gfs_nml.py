#!/usr/bin/env python
#################################################################################################
# Dependencies
#################################################################################################
import os
import argparse

#################################################################################################
# Command line arguments                                                      
#################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-nml1',   '--namelist1',   help='Namelist 1', required=True)
parser.add_argument('-nml2',   '--namelist2',   help='Namelist 2', required=True)

#################################################################################################
# 
#################################################################################################
def parse_arguments():
    """Parse command line arguments"""
    args        = parser.parse_args()
    nml_file1   = args.namelist1
    nml_file2   = args.namelist2
    return(nml_file1,nml_file2)

#################################################################################################
# Routine to read in GFS nml and store to python dictonary for comparision.
#################################################################################################
def read_nml(nml_file):
    gfs_nml_names = []
    gfs_nml_vals  = []
    nml = open(nml_file,'r')
    lines = nml.readlines()
    count = 0

    in_nml  = False
    for line in lines:
        if in_nml:
            line_tmp   = line.strip()
            line_splts = line_tmp.split('=')
            if line_tmp != "/":
                gfs_nml_names.append(line_splts[0].strip())
                gfs_nml_vals.append(line_splts[1].strip())
                count += 1
            # end if
        #end if
        if ("&gfs_physics_nml" in line.strip()): in_nml = True
        if ("/"                == line.strip()): in_nml = False
    # end for

    # Store nml to python dictionary.
    gfs_nml = []
    for inml in range(0,count):
        nml_dict = {}
        nml_dict["name"]   = gfs_nml_names[inml]
        nml_dict["values"] = gfs_nml_vals[inml]
        gfs_nml.append(nml_dict)
    # end for
    
    return(gfs_nml)
#################################################################################################
#
#################################################################################################
def cmp_nml(gfs_nml1, nml_file1, gfs_nml2, nml_file2, diff_count=0):
    diff_count = diff_count
    diff_this_time = True
    if (diff_count > 0): diff_this_time = False
    for nml1 in gfs_nml1:
        # For each entry in nml1,
        # - Is there an entry in nml2? If so, are they equivalent.
        found_nml1_in_nml2 = False
        for nml2 in gfs_nml2:
            if (nml1["name"] == nml2["name"]):
                found_nml1_in_nml2 = True
                if (diff_this_time and nml1["values"] != nml2["values"]):
                    diff_count = diff_count + 1
                    print("DIFFERENCE FOUND!",diff_count,diff_this_time)
                    print("   nml option: ", nml1["name"])
                    #print("     Found in ", nml_file1)
                    print("        with value(s) ", nml1["values"])
                    #print("     Differs from ", nml_file2)
                    print("        with value(s) ", nml2["values"])
                # end if
            # end if
        # end for
        if (not found_nml1_in_nml2):
            diff_count = diff_count + 1
            print("DIFFERENCE FOUND!",diff_count)
            print("nml option: ", nml1["name"])
            print("   Found in: ", nml_file1)
            #print("   with value(s) ", nml1["values"])
            print("   Missing from ", nml_file2)
        # end if
    # end for
    return(diff_count)

#################################################################################################
# Main 
#################################################################################################
# get nml file names.
(nml_file1, nml_file2) = parse_arguments()

# read in nml's
gfs_nml1 = read_nml(nml_file1)
gfs_nml2 = read_nml(nml_file2)

# compare nml's
print('#'*100)
diff_count = cmp_nml(gfs_nml1, nml_file1, gfs_nml2, nml_file2)
diff_count = cmp_nml(gfs_nml2, nml_file2, gfs_nml1, nml_file1, diff_count)

if (diff_count > 0):
    print(diff_count," DIFFERENCE FOUND")
else:
    print("No differences between namelists")
# end if
print('#'*100)
