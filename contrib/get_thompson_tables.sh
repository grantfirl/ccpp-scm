#!/bin/bash

set -ex

if [[ $(uname -s) == Darwin ]]; then
  if [[ $(sw_vers -productVersion) < 12.3 ]]; then
    MYDIR=$(cd "$(dirname "$(greadlink -f -n "${BASH_SOURCE[0]}" )" )" && pwd -P)
  else
    MYDIR=$(cd "$(dirname "$(readlink -f -n "${BASH_SOURCE[0]}" )" )" && pwd -P)
  fi
else
  MYDIR=$(cd "$(dirname "$(readlink -f -n "${BASH_SOURCE[0]}" )" )" && pwd -P)
fi
BASEDIR=$MYDIR/..

# Change to directory containing the physics input data, download and extract archive
cd $BASEDIR/scm/data/physics_input_data/
wget https://github.com/NCAR/ccpp-scm/releases/download/v6.0.0/thompson_tables2.tar
tar -xvf thompson_tables2.tar
rm -f thompson_tables2.tar
cd $BASEDIR/

