import numpy as np
import pandas as pd

def predictPrice(data: pd.core.frame.DataFrame) -> int:
	x = data['km']
	y = data['price']
	n = len(x)
	mean_x = sum(x) / n
	mean_y = sum(y) / n
	print(mean_x, mean_y)

	SS_xy = sum([(y[ind] * x[ind]) - (n * (mean_x) * (mean_y)) for ind in x.index])
	[print(x[ind], y[ind]) for ind in x.index]
	SS_xx = sum([(x[ind] * x[ind]) - n * ((mean_x) * (mean_x)) for ind in x.index])

	theta_1 = (SS_xy / SS_xx)
	theta_0 = (mean_y - (theta_1 * mean_x))
	
	return (theta_0, theta_1)