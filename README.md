# grixraz: mch GRIB archives as virtual Zarr stores

This is a proof-of-concept library that uses
[`kerchunk`](https://fsspec.github.io/kerchunk/) to represent MeteoSwiss GRIB archives
of NWP data as _virtual_ Zarr stores: no extracting, moving or copying.

You can find a demo in `notebooks/demo.ipynb` and an example of a reference file in `notebooks/example_reference_file.json`.

### Installation
- Run `source install_micromamba.sh` in order to install micromamba.
- Inside your source code folder, run `micromamba create -f environment.yaml` in order to setup the micromamba environment.
- Activate your environment by `micromamba activate grixraz`. Now you have installed eccodes and poetry.
- Install the dependencies managed by poetry: `poetry install`


### Running the demo
- valid user account on tsa
- git clone this repo, install in a new environment with [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

### As a developer
- also install the pre-commit hooks:
```pre-commit install```



### Opening the reference file from the demo
If you're in a rush and don't want to go through the demo, you can also just install `fsspec` (+ `xarray` and `zarr`) in your python environment and read the reference file from the example (it's on tsa).
```python
import json
import fsspec
import xarray as xr

with open("/scratch/fzanetta/grixraz/examples/kenda_anasurf_202306.json", "r") as f:
    ref = json.load(f)

fs = fsspec.filesystem("reference", fo=ref)
ds = xr.open_dataset(fs.get_mapper(""), engine="zarr", backend_kwargs=dict(consolidated=False),
                      chunks={'valid_time':1})
```