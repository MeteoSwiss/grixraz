from glob import glob
from itertools import product



def find_files(glob_pattern: str, expand: dict | None = None):
    """Find files matching a glob pattern, optionally expanding the pattern with a dict of values."""
    if expand is not None:
        expand = [dict(zip(expand.keys(), values)) for values in product(*expand.values())]
        files = []
        for exp in expand:
            files.extend(glob.glob(glob_pattern.format(**exp)))
        return sorted(glob(glob_pattern))
    else:
        return sorted(glob(glob_pattern))