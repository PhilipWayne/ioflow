from ioflow.corpus import get_corpus_processor
from ioflow.task_status import get_task_status
from ioflow.model_saver import get_model_saver
from ioflow.performance_metrics import get_performance_metrics
from ioflow.configure import read_configure

from dummy.input import build_input_func
from dummy.model import Model

config = read_configure()
model = Model(config)

task_status = get_task_status(config)

# read data according configure
corpus = get_corpus_processor(config)
corpus.prepare()
train_data_generator_func = corpus.get_generator_func(corpus.TRAIN)
eval_data_generator_func = corpus.get_generator_func(corpus.EVAL)

# send START status to monitor system
task_status.send_status(task_status.START)

# train and evaluate model
train_input_func = build_input_func(train_data_generator_func, config)
eval_input_func = build_input_func(eval_data_generator_func, config)

evaluate_result, export_results, final_saved_model = model.train_and_eval_then_save(
    train_input_func,
    eval_input_func,
    config
)

task_status.send_status(task_status.DONE)

if evaluate_result:
    performance_metrics = get_performance_metrics(config)
    performance_metrics.log_metric('test_loss', evaluate_result['loss'])
    performance_metrics.log_metric('test_acc', evaluate_result['acc'])

model_saver = get_model_saver(config)
model_saver.save_model(final_saved_model)
