from pylgnt.get_filepaths import get_filepaths
from pylgnt.constants.urls import OLD, NEW
from pylgnt.download import download


def main(_):
    urls = (OLD, NEW)
    filepaths = get_filepaths()
    for url, filepath in zip(urls, filepaths):
        download(url, filepath)
