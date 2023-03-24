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
    commands = list(handlers.keys())
    args = get_args(commands)
    command = args.command
    handler = handlers[command]
    handler(args)


def get_args(commands):
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=commands)
    return parser.parse_args()


if __name__ == "__main__":
    main()
