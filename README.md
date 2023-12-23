# grixraz: mch GRIB archives as virtual Zarr stores

This is a proof-of-concept library that uses
[`kerchunk`](https://fsspec.github.io/kerchunk/) to represent MeteoSwiss GRIB archives
of NWP data as _virtual_ Zarr stores: no extracting, moving or copying.

### Running the demo
- valid user account on tsa
- git clone this repo, install in a new environment with [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
