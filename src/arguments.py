from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description='Update projects'
    )
    parser.add_argument(
        "-i",
        "--ini",
        action="store",
        help="Update a single project with the ini config file."
    )

    parser.add_argument(
        "-c",
        "--config-directory",
        action="store",
        help="Directory where is the configs files located"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show what is going on"
    )

    parser.add_argument(
        "-vf",
        "--verbose-full",
        action="store_true",
        help="Show full detail on what is going on"
    )

    parser.add_argument(
        "-d",
        "--daemonize",
        action="store_true",
        help="Daemonize the updater"
    )

    return parser.parse_args()
