import os
from flask import render_template, current_app
from app.main import bp
from app.main.forms import UploadImageForm
from werkzeug.utils import secure_filename
from ada import utils, nn


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadImageForm()
    if form.validate_on_submit():
        file = form.image.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return render_template('index.html',
                               nn_state=f"Neural Network trained successfully. Accuracy is { utils.check_nn_score(nn)}",
                               nn_check_result=f"I think the number on image is { utils.recognize_img(nn, current_app.config['UPLOAD_FOLDER'] + filename)}",
                               form=form)
    return render_template('index.html',
                           nn_state=f"Neural Network trained successfully. Accuracy is { utils.check_nn_score(nn)}",
                           form=form)
