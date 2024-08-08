
## [1. MNIST Handwritten Digit Classifier with PyTorch](./1.MNIST_Handwritten_Digit_Classifier_with_PyTorch.ipynb).

This is a simple implementation of an image classifier using PyTorch. The classifier is designed to recognize handwritten digits from the MNIST dataset. The main components of the code include:
- Data Loading:
  Utilizes PyTorch's `datasets` and `DataLoader` to handle the MNIST dataset.
- Neural Network Architecture:
  Defines a convolutional neural network (CNN) with several convolutional layers followed by a fully connected layer for classification.
- Training: Implements a training loop to optimize the model using the `Adam` optimizer and `CrossEntropyLoss`.

- Prediction: Includes functionality to make predictions on new images and evaluate the trained model.
-  Model Details: The model is trained for 5 epochs. It's more efficient to use GPU.
