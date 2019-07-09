# performance_metrics 组件
## 功能
将训练过程中的 loss， accuracy, recall, f1 等信息报告并保存。

# 如何使用 performance_metrics 组件

```python
from ioflow.configure import read_config
from ioflow.performance_metrics import get_performance_metrics

config = read_config()

performance_metric = get_performance_metrics(config)

performance_metric.send_metrics(
    {"trainLoss": "2",
     "trainAccuray": "3",
     "testLoss": "4",
     "testAccuray": "66"}，
     step=1
)
```