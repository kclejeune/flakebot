#! /usr/bin/env python3

import os
import argparse
from pathlib import Path


def main(args):
    cwd = Path.cwd()
    flakes = (
        [flake for flake in [flake.parent for flake in cwd.glob("**/flake.nix")]]
        if args.recursive
        else [Path(f) for f in args.flakes]
    )

    if not flakes:
        print("no flakes provided")
        exit()

def run_update(path: Path):
    cmd = "nix flake update --recreate-lock-file --commit-lock-file"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--flakes",
        "-f",
        type=str,
        nargs="+",
        default=[Path.cwd()],
        help="the directorie(s) for flake.nix files to be updated",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="run flakebot recursively on any subdirectories with a flake.nix present",
    )
    args = parser.parse_args()
    main(args)
