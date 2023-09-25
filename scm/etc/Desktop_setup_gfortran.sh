#!/bin/bash

echo "Setting environment variables for CCPP-SCM on Desktop (MacOS) with gcc/gfortran"

MYDIR=$(cd "$(dirname "$(readlink -f -n "${BASH_SOURCE[0]}" )" )" && pwd -P)

export SCM_ROOT=$MYDIR/../..

echo "Setting CC/CXX/FC environment variables"
export CC=/opt/homebrew/bin/gcc
export CXX=/opt/homebrew/bin/g++
export FC=/opt/homebrew/bin/gfortran

echo "Setting location of NETCDF"
export NETCDF=/opt/homebrew
export LDFLAGS="-I${NETCDF}/include -L${NETCDF}/lib -Wl,-rpath,${NETCDF}/lib"

echo "Setting location of NCEPLIBS libraries"
export BACIO_LIB4=/Users/anders.jensen/hpc_stack/gnu-11.3.0/bacio/2.4.1/lib/libbacio_4.a
export SP_LIBd=/Users/anders.jensen/hpc_stack/gnu-11.3.0/sp/2.3.3/lib/libsp_d.a
export W3NCO_LIBd=/Users/anders.jensen/hpc_stack/gnu-11.3.0/w3nco/2.4.1/lib/libw3nco_d.a

export bacio_DIR=/Users/anders.jensen/hpc_stack/gnu-11.3.0/bacio/2.4.1/lib/cmake/bacio
export sp_DIR=/Users/anders.jensen/hpc_stack/gnu-11.3.0/sp/2.3.3/lib/cmake/sp
export w3emc_DIR=/Users/anders.jensen/hpc_stack/gnu-11.3.0/w3emc/2.9.2/lib/cmake/w3emc
