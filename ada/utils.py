from ada import config
import imageio
import numpy as np


def train_nn(neural_network, epochs):

    with open(config.TRAIN_DATA_PATH, "r") as train_data_file:
        train_dataset = train_data_file.readlines()

    for epoch in range(epochs):
        for row in train_dataset:
            all_values = row.split(",")
            inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = np.zeros(config.NN_OUTPUT_NODES) + 0.01
            targets[int(all_values[0])] = 0.99
            neural_network.train(inputs, targets)
    return neural_network


def check_nn_score(neural_network):
    scorecard = []
    with open(config.TEST_DATA_PATH, "r") as test_data_file:
        test_dataset = test_data_file.readlines()
    for row in test_dataset:
        all_values = row.split(",")
        correct_label = int(all_values[0])

        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = neural_network.query(inputs)
        predicted_label = np.argmax(outputs)

        if correct_label == predicted_label:
            scorecard.append(1)
        else:
            scorecard.append(0)
    scorecard_arr = np.asarray(scorecard)
    return scorecard_arr.sum() / scorecard_arr.size


def recognize_img(neural_network, image_path):
    outputs = neural_network.query(img_to_matrix(image_path))
    return np.argmax(outputs)


def img_to_matrix(image_path):
    img_array = imageio.imread(image_path, as_gray=True)
    img_data = 255.0 - img_array.reshape(784)
    return (img_data / 255.0 * 0.99) + 0.01

