import json
import os


def read_json_file(json_file):
    if not os.path.exists(json_file):
        return None

    with open(json_file) as fd:
        return json.load(fd)


def read_configure() -> dict:
    active_configure_file = os.getenv('_DEFAULT_CONFIG_FILE', './configure.json')

    active_configure = read_json_file(active_configure_file)

    print(active_configure)

    return active_configure

    # sys.exit(0)

    # return {
    #     'corpus': {
    #         'train': './data/train.conllz',
    #         'test': './data/test.conllz'
    #     },
    #     'model': {
    #         'shuffle_pool_size': 10,
    #         'batch_size': 32,
    #         'epochs': 20,
    #         'arch': {}
    #      }
    # }
