#!/usr/bin/env python3
"""PyGram

Usage:
  pygram hello [--log-level=<level>]
  pygram (-h | --help)
  pygram --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --log-level=<level>  Logging level verbosity [default: info].

"""
import logging
import json
from typing import Callable

from docopt import docopt


def setup_logger(level_name):
    level = logging.getLevelName(level_name.upper())
    logging.basicConfig(
        level=level, format="%(name)s - %(levelname)s - %(message)s",
    )


def hello(**kwargs):
    print("hello")
    print(f"kwargs: {json.dumps(kwargs, indent=2)}")


def main():
    args = docopt(__doc__, version="Naval Fate 2.0")
    setup_logger(args["--log-level"])

    for func_name, func in filter(
        lambda kv: isinstance(kv[1], Callable), globals().items()
    ):
        if func_name in args and args[func_name]:
            func(**args)
