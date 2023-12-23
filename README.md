# grixraz: mch GRIB archives as virtual Zarr stores

This is a proof-of-concept library that uses
[`kerchunk`](https://fsspec.github.io/kerchunk/) to represent MeteoSwiss GRIB archives
of NWP data as _virtual_ Zarr stores: no extracting, moving or copying.

You can find a demo in `notebooks/demo.ipynb` and an example of a reference file in `notebooks/example_reference_file.json`.

### Running the demo
- valid user account on tsa
- git clone this repo, install in a new environment with [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
