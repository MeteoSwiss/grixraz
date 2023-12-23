from pathlib import Path
from kerchunk.grib2 import scan_grib
from concurrent.futures import ThreadPoolExecutor
from tqdm.auto import tqdm
import ujson # like json, but ultra faster


def make_json_name(file: str, message_number: int):
    """Make a json name from a file name and message number."""
    name = file.split("/")[-1]
    return f"{name}_message{message_number:03}.json"


def create_references(
    files: list[str], out_dir: str = "references/", n_workers=5, **scan_kwargs
):
    """Create references for a list of files."""
    out_dir = Path(out_dir)
    out_dir.mkdir(exist_ok=True, parents=True)

    def gen_json(file_url):
        """Generate a json reference for a single file."""
        out = scan_grib(file_url, **scan_kwargs)
        messages = []
        for i, message in enumerate(out):
            out_file_name = make_json_name(file_url, i)
            fn = out_dir / out_file_name
            with open(fn, "w") as f:
                f.write(ujson.dumps(message, indent=4))
            messages.append(fn.as_posix())
        return messages
    
    # for an obscure reason we have to do this
    gen_json(files[0])

    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        results = list(tqdm(executor.map(gen_json, files), desc = "Creating references...", total=len(files)))

    # flatten the list
    results = [msg for fn in results for msg in fn]

    return results


def get_references(ref_dir: str = "references/"):
    """Get references from a directory."""
    ref_dir = Path(ref_dir)
    files = list(ref_dir.glob("*.json"))
    return files