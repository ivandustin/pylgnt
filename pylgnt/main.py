import argparse
from .handle_download import handle_download
from .handle_convert import handle_convert
from .handle_extract import handle_extract


def main():
    handlers = {
        "download": handle_download,
        "convert": handle_convert,
        "extract": handle_extract,
    }
    args = get_args()
    command = args.command
    handler = handlers[command]
    handler(args)


def get_args():
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers(dest="command", required=True)
    parsers.add_parser("download")
    parsers.add_parser("convert")
    extract = parsers.add_parser("extract")
    extract.add_argument("directory")
    return parser.parse_args()


if __name__ == "__main__":
    main()
