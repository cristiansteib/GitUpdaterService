from argparse import  ArgumentParser
from updater import Updater

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
    return parser.parse_args()


def run():
    arguments = parse_args()
    if arguments.ini:
        Updater(the_file=arguments.ini)
    elif arguments.config_directory:
        Updater(configs_directory=arguments.config_directory)


if __name__ == "__main__":
    run()