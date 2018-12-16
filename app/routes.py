from flask import render_template
from app import app
import numpy as np
from app.models import NeuralNetwork


@app.route('/')
@app.route('/index')
def index():
    scorecard = []

    nn = NeuralNetwork(app.config['NN_INPUT_NODES'],
                       app.config['NN_HIDDEN_NODES'],
                       app.config['NN_OUTPUT_NODES'],
                       app.config['NN_LEARNING_RATE'])

    with open(app.config['TRAIN_DATA_PATH'], "r") as train_data_file:
        train_dataset = train_data_file.readlines()

    for epoch in range(app.config['NN_LEARN_EPOCHS']):
        for row in train_dataset:
            all_values = row.split(",")
            inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = np.zeros(app.config['NN_OUTPUT_NODES']) + 0.01
            targets[int(all_values[0])] = 0.99
            nn.train(inputs, targets)

    with open(app.config['TEST_DATA_PATH'], "r") as test_data_file:
        test_dataset = test_data_file.readlines()

    for row in test_dataset:
        all_values = row.split(",")
        correct_label = int(all_values[0])

        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        predicted_label = np.argmax(outputs)

        if correct_label == predicted_label:
            scorecard.append(1)
        else:
            scorecard.append(0)

    scorecard_arr = np.asarray(scorecard)
    return render_template('index.html',
                           message=f"Accuracy of neural network is {scorecard_arr.sum() / scorecard_arr.size}")
