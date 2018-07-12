from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description='This script is the runneer for the updater,'
                    'if no parameter is set, it will going to use the conf/config.ini file'
    )
    parser.add_argument(
        "-i",
        "--ini",
        action="store",
        help="Update a single project with the ini config file."
    )

    parser.add_argument(
        "-c",
        "--configs-directory",
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
        "-web",
        "--web",
        action="store_true",
        default=False,
        help="Activate the web listener"
    )
    return parser.parse_args()
