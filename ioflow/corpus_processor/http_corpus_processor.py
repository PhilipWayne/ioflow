import functools

import requests
import numpy as np
from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.tagset.offset.span_set import SpanSet
from tokenizer_tools.tagset.offset.span import Span

from ioflow.corpus_processor.corpus_processor_base import CorpusProcessorBase
from ioflow.corpus import Corpus


def parse(obj):
    span_set = SpanSet()
    for span in obj.spans:
        span_obj = Span(start=span.start, end=span.end, entity=span.type)
        span_set.append(span_obj)

    label = obj.label
    seq = Sequence(text=obj.text, span_set=span_set, label=label)

    return seq


def generator_fn(config):
    r = requests.get(config['data_url'], params={'task_id': config['task_id']})
    sentence_list = r.json()

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
