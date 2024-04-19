#!/bin/bash

path=$HOME/eccodes-cosmo-resources

if [ ! -d ${path} ]; then
    # branch that implements the mars model needed for FDB
    git clone -b revise_mars_model https://github.com/cosunae/eccodes-cosmo-resources.git ${path}
fi
