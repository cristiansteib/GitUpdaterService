from argparse import ArgumentParser
from modules.updater import Updater


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
    return parser.parse_args()


def run():
    arguments = parse_args()
    kwargs = {
        'the_file': arguments.ini,
        'configs_directory': arguments.config_directory,
        'verbose': arguments.verbose,
        'full_verbose': arguments.verbose_full
    }

    Updater(**kwargs)


if __name__ == "__main__":
    run()
