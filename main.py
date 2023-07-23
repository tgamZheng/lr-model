import numpy as np
from sklearn.linear_model import LinearRegression

def train():
    # Sample data: a simple sequence from 1 to 10
    X = np.array([[i] for i in range(1, 15)])
    y = np.array([i * 2 for i in range(1, 15)])

    # Initialize the linear regression model
    model = LinearRegression()

    # Train the model on the data
    model.fit(X, y)

    return model

def predict(model,input:int) -> int:
    # Predict the next value in the sequence (11)
    next_value = model.predict([[input]])[0]
    print(f"Predicted next value in the sequence: {next_value:.2f}")
    return int


if __name__ == "__main__":
    model = train()
    predict(model, input=11)
