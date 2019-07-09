# corpus 组件
## 工作原理
corpus 将各种格式（纯文本、JSON 等）和存储方案（本地，远程HTTP, S3 等）的语料数据 统一转换成 offset 对象。
用户再从 offset 对象生成自己想要的数据格式或者对象。

同事，附加了训练集和测试集分拆和收集元信息等助手功能

# 如何使用 corpus 组件

```python
from ioflow.configure import read_config
from ioflow.corpus import get_corpus_processor

config = read_config()

corpus_processor = get_corpus_processor(config)
corpus_processor.prepare()

train_data_generator_func = corpus_processor.get_generator_func(corpus.TRAIN)
eval_data_generator_func = corpus_processor.get_generator_func(corpus.EVAL)

corpus_meta_data = corpus_processor.get_meta_info()

for corpus in train_data_generator_func():
    print("corpus as offset object: {}".format(corpus))

print("tags: {}; labels: {}".format(corpus_meta_data['tags'], corpus_meta_data['labels'])
```