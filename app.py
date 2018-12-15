from model import NeuralNetwork
import numpy as np
import matplotlib.pyplot as plt
import config

if __name__ == "__main__":
    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10
    learning_rate = 0.2

    epochs = 2

    scorecard = []

    nn = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    with open(config.DATASETS_REPO + "mnist_train.csv", "r") as train_data_file:
        train_dataset = train_data_file.readlines()

    for epoch in range(epochs):
        for row in train_dataset:
            all_values = row.split(",")
            inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = np.zeros(output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99
            nn.train(inputs, targets)

    with open(config.DATASETS_REPO + "mnist_test.csv", "r") as test_data_file:
        test_dataset = test_data_file.readlines()

    for row in test_dataset:
        all_values = row.split(",")
        correct_label = int(all_values[0])
        # print(f"True label is {correct_label}")

        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        predicted_label = np.argmax(outputs)
        # print(f"Predicted label is {predicted_label}")

        if correct_label == predicted_label:
            scorecard.append(1)
        else:
            scorecard.append(0)
            pass

    scorecard_arr = np.asarray(scorecard)
    print(f"Accuracy of neural network is {scorecard_arr.sum()/scorecard_arr.size}")
