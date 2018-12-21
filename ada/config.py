import os

basedir = os.path.abspath(os.path.dirname(__file__))

NN_INPUT_NODES = int(os.environ.get('NN_INPUT_NODES') or 784)
NN_HIDDEN_NODES = int(os.environ.get('NN_HIDDEN_NODES') or 100)
NN_OUTPUT_NODES = int(os.environ.get('NN_OUTPUT_NODES') or 10)
NN_LEARNING_RATE = float(os.environ.get('NN_LEARNING_RATE') or 0.2)
