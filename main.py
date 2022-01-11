# GENERAL LIBRARIES
import os
import numpy as np
import argparse
# MACHINE LEARNING LIBRARIES
import tensorflow as tf
# CUSTOM LIBRARIES
from utils.tools import read_yaml, Logger
from utils.trainer import Trainer


# LOAD CONFIG 
parser = argparse.ArgumentParser(description='Process some input')
parser.add_argument('--config', default='utils/config.yaml', type=str, help='Config path', required=False)    
parser.add_argument('--benchmark','-b', action='store_true', help='Run a benchmark') 
parser.add_argument('--search','-s', action='store_true', help='Run a random search')
    
args = parser.parse_args()
config = read_yaml(args.config)
logger = Logger(config['LOG_FILE'])


# SET GPU 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_visible_devices(gpus[config['GPU']], 'GPU')
tf.config.experimental.set_memory_growth(gpus[config['GPU']], True)


# SET TRAINER
trainer = Trainer(config, logger)

if args.benchmark:
    # RUN BENCHMARK
    trainer.do_benchmark()

elif args.search:
    # RUN RANDOM SEARCH
    trainer.do_random_search()
    
else:
    print('Nothing to do! Specify one of the following arguments:')
    print('\t --benchmark [-b]: run a benchmark')
    print('\t --search [-s]: run a random search')