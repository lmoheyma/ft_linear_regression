from leastSquareEstimation import estimatePrice
import pandas as pd

def gradientDescent(alpha: float, data: pd.core.frame.DataFrame):
	count = 1000
	i = 0
	m = len(data)
	theta0, theta1 = 0
	mileage = data['km']
	price = data['price']
	while(i < count):
		theta0 -= alpha * ((1 / m) * sum(estimatePrice(mileage[i]) - price[i]))
		theta1 -= alpha * ((1 / m) * sum(estimatePrice(mileage[i]) - price[i]) * mileage[i])
		i += 1