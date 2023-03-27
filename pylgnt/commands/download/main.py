from pylgnt.get_filepaths import get_filepaths
from pylgnt.download_url import download_url
from pylgnt.constants.urls import OLD, NEW


def main(_):
    urls = (OLD, NEW)
    filepaths = get_filepaths()
    for url, filepath in zip(urls, filepaths):
        download_url(url, filepath)
