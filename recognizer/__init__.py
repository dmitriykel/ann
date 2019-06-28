from recognizer import model, config, utils

utils.download_data(config.TRAIN_DATA_URL, config.TEST_DATA_URL)
ann = model.NeuralNetwork(config.NN_INPUT_NODES,
                          config.NN_HIDDEN_NODES,
                          config.NN_OUTPUT_NODES,
                          config.NN_LEARNING_RATE)
nn = utils.train_nn(ann, config.NN_LEARN_EPOCHS)
