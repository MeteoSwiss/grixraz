#!/bin/bash

path=$HOME/eccodes-cosmo-resources

if [ ! -d ${path}]; then
    git clone -b revise_mars_model git@github.com:cosunae/eccodes-cosmo-resources.git ${path}
fi

export ECCODES_DEFINITIONS_PATH=$CONDA_PREFIX/share/eccodes/definitions
