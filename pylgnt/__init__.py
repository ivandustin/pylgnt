import argparse
from .commands.normalize.main import main as normalize_main
from .commands.alphabet.main import main as alphabet_main
from .commands.download.main import main as download_main
from .commands.convert.main import main as convert_main
from .commands.extract.main import main as extract_main
from .commands.info.main import main as info_main


def main():
    handlers = {
        "normalize": normalize_main,
        "alphabet": alphabet_main,
        "download": download_main,
        "convert": convert_main,
        "extract": extract_main,
        "info": info_main,
    }
    args = get_args()
    command = args.command
    handler = handlers[command]
    handler(args)


def get_args():
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers(dest="command", required=True)
    parsers.add_parser("normalize")
    alphabet = parsers.add_parser("alphabet")
    alphabet.add_argument("--normalize", action="store_true")
    parsers.add_parser("download")
    parsers.add_parser("convert")
    parsers.add_parser("info")
    extract = parsers.add_parser("extract")
    extract.add_argument("directory")
    return parser.parse_args()


if __name__ == "__main__":
    main()
