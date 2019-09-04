import argparse


def get_configure_path_from_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ioflow_default_configure', type=str, nargs='?', help='specific default configure file location')

    args = parser.parse_args()

    return args.ioflow_default_configure


if __name__ == "__main__":
    get_configure_path_from_argv()