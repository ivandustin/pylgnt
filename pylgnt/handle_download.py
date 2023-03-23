from pathlib import Path
from .constants import OT_URL, NT_URL, OT_NAME, NT_NAME
from .download_url import download_url


def handle_download(_):
    urls = [(OT_URL, Path(OT_NAME)), (NT_URL, Path(NT_NAME))]
    for url, filepath in urls:
        download_url(url, filepath)
