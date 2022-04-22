#!/usr/bin/env python3
"""Command line hello world"""

import argparse


def get_args():
    """Get optional arguments from command line"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main() -> int:
    """Greet someone"""
    args = get_args()
    print(f"Hello, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
