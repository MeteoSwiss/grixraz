#!/bin/bash

prefix=$HOME/.local/bin

mkdir -p ${prefix} && wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvjf - -C ${prefix} bin/micromamba --strip-components 1
${prefix}/micromamba shell init -s bash -p $SCRATCH/micromamba
source ~/.bashrc
