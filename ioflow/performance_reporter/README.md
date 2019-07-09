# performance_reporter 组件
## 功能
将评估过程中的 loss， accuracy, recall, f1 等信息报告并保存。

# 如何使用 performance_reporter 组件

```python
from ioflow.configure import read_config
from ioflow.performance_reporter import get_performance_reporter

config = read_config()

performance_reporter = get_performance_reporter(config)

performance_reporter.send_performances(
    {"trainLoss": "2",
     "trainAccuray": "3",
     "testLoss": "4",
     "testAccuray": "66"}
)
```