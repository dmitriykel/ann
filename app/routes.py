from flask import render_template
from app import app, utils


@app.route('/')
@app.route('/index')
def index():
    nn = utils.train_nn(app.config['NN_INPUT_NODES'],
                   app.config['NN_HIDDEN_NODES'],
                   app.config['NN_OUTPUT_NODES'],
                   app.config['NN_LEARNING_RATE'],
                   app.config['NN_LEARN_EPOCHS'])
    return render_template('index.html',
                           message=f"Neural Network trained successfully. Accuracy is {utils.check_nn_score(nn)}")


@app.route('/recognition')
def recognition():
    nn = utils.train_nn(app.config['NN_INPUT_NODES'],
                        app.config['NN_HIDDEN_NODES'],
                        app.config['NN_OUTPUT_NODES'],
                        app.config['NN_LEARNING_RATE'],
                        app.config['NN_LEARN_EPOCHS'])
    return render_template('recognition.html',
                           message=f"This is number {utils.recognize_img(nn, 'static/6.png')}",
                           img_filename="6.png")
