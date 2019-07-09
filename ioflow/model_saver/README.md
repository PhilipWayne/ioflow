# model_saver 组件
## 功能
将训练过程中的当前运行状态报告并保存。

# 如何使用 model_saver 组件

```python
from ioflow.configure import read_config
from ioflow.model_saver import get_model_saver

config = read_config()

model_saver = get_model_saver(config)

model_saver.save_model("path/to/model/dir")
```