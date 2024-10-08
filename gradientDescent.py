from leastSquareEstimation import estimatePrice
import pandas as pd

def gradientDescent(learningRate: float, data: pd.core.frame.DataFrame):
	count = 1000
	i = 0
	m = len(data)
	while(i < count):
		tmpTheta0 = learningRate * (1 / m) * sum(estimatePrice())
		tmpTheta1 = 0
		i += 1