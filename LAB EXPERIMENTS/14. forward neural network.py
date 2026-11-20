
import numpy as np

# Input data
X = np.array([[0, 0], [0, 1],
              [1, 0], [1, 1]])

Y = np.array([[0], [1], [1], [0]])

# Initialize weights
np.random.seed(1)
w1 = np.random.rand(2, 2)
w2 = np.random.rand(2, 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Training
for i in range(10000):

    hidden = sigmoid(np.dot(X, w1))
    output = sigmoid(np.dot(hidden, w2))

    error = Y - output

    d_output = error * output * (1 - output)
    d_hidden = np.dot(d_output, w2.T) * hidden * (1 - hidden)

    w2 += np.dot(hidden.T, d_output) * 0.5
    w1 += np.dot(X.T, d_hidden) * 0.5

# Final prediction
print("Predicted Output:")
print(np.round(output, 2))
