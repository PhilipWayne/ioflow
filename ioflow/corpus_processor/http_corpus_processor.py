import functools

import requests
import numpy as np
from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.tagset.offset.span_set import SpanSet
from tokenizer_tools.tagset.offset.span import Span

from ioflow.corpus_processor.corpus_processor_base import CorpusProcessorBase
from ioflow.corpus import Corpus


def parse(obj):
    # find entity
    entity = None
    for entity in obj['annotations']:
        if entity['labels_type'] == 'slot':
            break

    # find label class_
    class_ = None
    for class_ in obj['annotations']:
        if class_['labels_type'] == 'classify':
            break

    span_set = SpanSet()
    for span in entity['entities']:
        span_obj = Span(start=int(span['start_index']), end=(int(span['start_index']) + int(span['slot_len'])), entity=span['slot_value'])
        span_set.append(span_obj)

    label = class_['classify']
    seq = Sequence(text=obj['text'], span_set=span_set, label=label)

    return seq


def generator_fn(config):
    r = requests.post(config['data_url'], json={'taskId': config['task_id']})
    sentence_list = r.json()['data']

    for sentence in sentence_list:
        offset_data = parse(sentence)

        yield offset_data


def request_meta_data(config):
    r = requests.get(config['meta_data_url'], params={'task_id': config['task_id']})
    return r.json()


class HttpCorpusProcessor(CorpusProcessorBase):
    def __init__(self, config):
        super(HttpCorpusProcessor, self).__init__(config)
        self.dataset_mapping = {}

    def prepare(self):
        self.dataset_mapping[Corpus.TRAIN] = functools.partial(generator_fn, self.config)

    def get_generator_func(self, data_set):
        return self.dataset_mapping[data_set]

    def get_meta_info(self):
        return request_meta_data(self.config)


if __name__ == "__main__":
    config = {
        'data_url': 'http://10.43.10.48:8110/algo/corpusManger/getCorpusByTrainingTaskId',
        'task_id': '5cd536215148635cc0fe29e2'
    }

    processor = HttpCorpusProcessor(config)
    processor.prepare()
    gfunc = processor.get_generator_func(Corpus.TRAIN)

    for i in gfunc():
        print(i)