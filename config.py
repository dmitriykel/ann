import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'upload/'
    TRAIN_DATA_PATH = os.environ.get('TRAIN_DATA_PATH') or os.path.join(basedir, 'datasets/mnist_train.csv')
    TEST_DATA_PATH = os.environ.get('TEST_DATA_PATH') or os.path.join(basedir, 'datasets/mnist_test.csv')
    NN_LEARN_EPOCHS = int(os.environ.get('NN_LEARN_EPOCHS') or 2)
