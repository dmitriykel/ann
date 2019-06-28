import os

basedir = os.path.abspath(os.path.dirname(__file__))

NN_INPUT_NODES = int(os.environ.get('NN_INPUT_NODES') or 784)
NN_HIDDEN_NODES = int(os.environ.get('NN_HIDDEN_NODES') or 100)
NN_OUTPUT_NODES = int(os.environ.get('NN_OUTPUT_NODES') or 10)
NN_LEARNING_RATE = float(os.environ.get('NN_LEARNING_RATE') or 0.2)
NN_LEARN_EPOCHS = int(os.environ.get('NN_LEARN_EPOCHS') or 2)
TRAIN_DATA_PATH = os.environ.get('TRAIN_DATA_PATH') or os.path.join(basedir, 'datasets/mnist_train.csv')
TEST_DATA_PATH = os.environ.get('TEST_DATA_PATH') or os.path.join(basedir, 'datasets/mnist_test.csv')
TRAIN_DATA_URL = os.environ.get('TRAIN_DATA_URL') or 'https://pjreddie.com/media/files/mnist_train.csv'
TEST_DATA_URL = os.environ.get('TEST_DATA_URL') or 'https://pjreddie.com/media/files/mnist_train.csv'
