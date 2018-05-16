# Simple Linear Regression 

"""
Theory:-

y = B0 + B1 * x

y = value to be predicted
x = dependent value
B1 = slope
B0 = intercept 

Formulae:-

B1 = sum((xi - mean(x)) * (yi - mean(y))) / sum((xi - mean(x)) ^ 2) 
B0 = mean(y) - B1 * mean(x)

"""
import numpy as np

class slr:
    B0 = 0
    B1 = 0
    def fit(self, X, y):
        self.B1 = np.sum((X - np.mean(X)) * (np.reshape((y - np.mean(y)), (20, 1)))) / np.sum(pow(
                (X - np.mean(X)), 2))
        self.B0 = np.mean(y) - self.B1 * np.mean(X)
        print("Fit successful to training set!")
        print("Intercept = " + str(self.B0))
        print("Slope = " + str(self.B1))
        
    def predict(self, X, accuracy=2):
        y_pred = []
        y_pred = self.B0 + self.B1 * X
        y_pred = np.around(y_pred, decimals = accuracy)
        return y_pred
        