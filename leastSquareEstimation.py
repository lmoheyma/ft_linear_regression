from matplotlib import pyplot as plt
import pandas as pd

def displayLinearRegression(x: float, y: float, theta0: float, theta1: float) -> int:
	plt.scatter(x, y)
	linearRegression = theta0 + (theta1 * x)
	plt.plot(x, linearRegression, color='red')

def estimatePrice(data: pd.core.frame.DataFrame) -> int:
	x = data['km']
	y = data['price']
	n = len(x)
	mean_x = sum(x) / n
	mean_y = sum(y) / n

	SS_xy = sum([(y[ind] * x[ind]) for ind in x.index]) - (n * (mean_x) * (mean_y))
	SS_xx = sum([(x[ind] * x[ind]) for ind in x.index]) - n * ((mean_x) * (mean_x)) 

	theta_1 = (SS_xy / SS_xx)
	theta_0 = (mean_y - (theta_1 * mean_x))
	displayLinearRegression(x, y, theta_0, theta_1)
	return (theta_0, theta_1)
