from matplotlib import pyplot as plt
import pandas as pd

def displayLinearRegression(x: float, y: float, theta0: float, theta1: float) -> int:
	plt.scatter(x, y)
	linearRegression = theta0 + (theta1 * x)
	plt.plot(x, linearRegression, color='red')
