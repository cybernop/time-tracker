from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")

    track_parser = subparsers.add_parser("track", description="Time tracking")
    group = track_parser.add_mutually_exclusive_group()
    group.add_argument("--start", action="store_true", help="Start tracking")
    group.add_argument("--stop", action="store_true", help="Stop tracking")

    return parser.parse_args()
