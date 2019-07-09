# task_status 组件
## 功能
将训练过程中的当前运行状态报告并保存。

# 如何使用 task_status 组件

```python
from ioflow.configure import read_config
from ioflow.performance_metrics import get_task_status

config = read_config()

task_status = get_task_status(config)

task_status.send_status(ts.START)
```