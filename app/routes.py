import os
from flask import render_template, redirect, url_for
from app import app, utils
from app.forms import UploadImageForm
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadImageForm()
    nn = utils.train_nn(app.config['NN_INPUT_NODES'],
                        app.config['NN_HIDDEN_NODES'],
                        app.config['NN_OUTPUT_NODES'],
                        app.config['NN_LEARNING_RATE'],
                        app.config['NN_LEARN_EPOCHS'])

    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html',
                               nn_state=f"Neural Network trained successfully. Accuracy is {utils.check_nn_score(nn)}",
                               nn_check_result=f"I think the number on image is {utils.recognize_img(nn, app.config['UPLOAD_FOLDER'] + filename)}",
                               form=form)
    return render_template('index.html',
                           nn_state=f"Neural Network trained successfully. Accuracy is {utils.check_nn_score(nn)}",
                           form=form)


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
