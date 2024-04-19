import eccodes
import grixraz


def test_grib_varnames():
    file = "/scratch/fzanetta/tmp/hackathon/lafsurf2023083123_det"
    varnames = set()
    with open(file, "rb") as gribfile:
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
