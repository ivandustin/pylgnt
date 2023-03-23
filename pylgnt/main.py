import argparse
from .handle_download import handle_download
from .handle_convert import handle_convert

handlers = {
    "download": handle_download,
    "convert": handle_convert,
}


def main():
    args = get_args()
    command = args.command
    handler = handlers[command]
    handler(args)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=list(handlers.keys()))
    return parser.parse_args()


if __name__ == "__main__":
    main()
