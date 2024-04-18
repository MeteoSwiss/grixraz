from pathlib import Path
from functools import partial
from kerchunk.grib2 import scan_grib
from kerchunk.combine import merge_vars
from concurrent.futures import ThreadPoolExecutor
from tqdm.auto import tqdm
import ujson  # like json, but ultra faster


def make_json_name(file: str, message: dict[str, str]):
    """Make a json name from a file name and message number."""
    name = file.split("/")[-1]
    var = list(message["refs"].keys())[2].split("/")[0]
    return f"{name}_{var}.json"


def var_refs(file_url, out_dir, **scan_kwargs):
    """Generate a json references for messages in a file."""
    messages = []
    for message in scan_grib(file_url, **scan_kwargs):
        out_file_name = make_json_name(file_url, message)
        fn = out_dir / out_file_name
        with open(fn, "w") as f:
            f.write(ujson.dumps(message, indent=4))
        messages.append(fn.as_posix())
    return messages


def merged_var_refs(grib_filename, out_dir, **scan_kwargs):
    """Generate a json reference for a single file, merging all messages."""
    ref = merge_vars(scan_grib(grib_filename, **scan_kwargs))
    fn = out_dir / f"{grib_filename.split('/')[-1]}.json"
    with open(fn, "w") as f:
        f.write(ujson.dumps(ref, indent=4))
    return fn.as_posix()


def create_references(
    files: list[str],
    out_dir: str = "references/",
    n_workers=5,
    merge_messages: bool = True,
    **scan_kwargs,
):
    """Create references for a list of files."""
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True, parents=True)

    ref_fn = merged_var_refs if merge_messages else var_refs
    ref_fn = partial(ref_fn, out_dir=out_dir, **scan_kwargs)

    # for an obscure reason we have to do this
    ref_fn(files[0])

    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        results = list(
            tqdm(
                executor.map(ref_fn, files),
                desc="Creating references...",
                total=len(files),
            )
        )

    # flatten the list
    if not merge_messages:
        results = [msg for fn in results for msg in fn]

    return results


def get_references(ref_dir: str = "references/"):
    """Get references from a directory."""
    ref_dir = Path(ref_dir)
    files = list(ref_dir.glob("*.json"))
    return files
