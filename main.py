"""module doc: this module has lr model train predict func"""

import numpy as np
from sklearn.linear_model import LinearRegression

def train():
    """train function
    Params:
    a
    b
    c

    Returns:
        _type_: _description_
    """
    # Sample data: a simple sequence from 1 to 10
    X = np.array([[i] for i in range(1, 13)])
    y = np.array([i * 2 for i in range(1, 13)])

    # Initialize the linear regression model
    model = LinearRegression()

    # Train the model on the data
    model.fit(X, y)

    return model

def predict(model,input:int) -> int:
    """_summary_

    Args:
        model (_type_): lr model object
        input (int): an arb int

    Returns:
        int: predicted value(int)
    """
    # Predict the next value in the sequence (11)
    next_value = model.predict([[input]])[0]
    print(f"Predicted next value in the sequence: {next_value:.2f}")
    return int


if __name__ == "__main__":
    model = train()
    predict(model, input=11)
