from urllib.request import Request, urlopen
from tempfile import TemporaryDirectory
from pathlib import Path
from shutil import move


def download_url(url, filepath):
    request = Request(url)
    request.add_header("User-Agent", "Mozilla/5.0")
    with urlopen(request) as response:
        with TemporaryDirectory() as tempdir:
            tempdir = Path(tempdir)
            tempfile = tempdir / filepath.name
            with open(tempfile, "wb") as file:
                file.write(response.read())
            move(tempfile, filepath)
