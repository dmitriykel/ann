from ada import model, config

ada = model.NeuralNetwork(config.NN_INPUT_NODES,
                          config.NN_HIDDEN_NODES,
                          config.NN_OUTPUT_NODES,
                          config.NN_LEARNING_RATE)
