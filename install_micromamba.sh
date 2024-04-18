mkdir -p ~/.local/bin && wget -qO- https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvjf - -C ~/.local/ bin/micromamba
~/.local/bin/micromamba shell init -s bash -p $SCRATCH/micromamba 
source ~/.bashrc
