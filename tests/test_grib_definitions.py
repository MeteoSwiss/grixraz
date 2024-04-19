import os
from pathlib import Path
import eccodes
import grixraz  # noqa


def test_grib_varnames():
    # we want to make sure that variable names are translated according to the eccodes COSMO definition
    file_path = os.path.join(Path(__file__).parent, 'data', 'grib_test_file')
    varnames = set()
    with open(file_path, "rb") as gribfile:
        while True:
            message_id = eccodes.codes_grib_new_from_file(gribfile)
            if message_id is None:
                break
            # Retrieve shortName for the parameter,
            # which is commonly used as the variable name
            shortName = eccodes.codes_get(message_id, "shortName")
            varnames.add(shortName)
            eccodes.codes_release(message_id)
    # We could expand to check the full set of varnames, but at the moment
    # it is not known what the full correct set would be. :-/
    assert "T_2M" in varnames
