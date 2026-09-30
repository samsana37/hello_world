from sklearn.linear_model import LinearRegression
import numpy as np

def train():
    # Training data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    # Create and train model
    model = LinearRegression()
    model.fit(X, y)

    return model