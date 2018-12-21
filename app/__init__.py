from flask import Flask
from config import Config
from ada import ada
import app.utils

nn = utils.train_nn(ada, 2)
app = Flask(__name__)
app.config.from_object(Config)

from app import routes
