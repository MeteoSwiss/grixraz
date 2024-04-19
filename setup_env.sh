#!/bin/bash

path=$HOME/eccodes-cosmo-resources

if [ ! -d ${path} ]; then
    git clone -b revise_mars_model git@github.com:cosunae/eccodes-cosmo-resources.git ${path}
fi
