from leastSquareEstimation import estimatePrice
from load_csv import load
import pandas as pd


class LinearRegression:
	def __init__(self) -> None:
		self.theta0 = 0.0
		self.theta1 = 0.0
		self.data = load("data.csv")
		self.dataMileages = self.data['km']
		self.dataPrices = self.data['price']
		self.scaledMileages = self.scaledMileages()
	
	def scaledMileages(self):
		N = len(self.data)
		meanMileages = sum(self.dataMileages) / N
		stdDeviation = (sum([(mileage - meanMileages)**2 for mileage in self.dataMileages]) / N)**0.5
		return [(mileage - meanMileages) / stdDeviation for mileage in self.dataMileages]


	def estimatePrice(self, theta0, theta1, mileage) -> float:
		try:
			mileage = float(mileage)
		except ValueError:
			print("Type Error")
			exit(1)
		return float(theta0 + (theta1 * mileage))


	def lossFunction(self):
		errors0 = []
		errors1 = []
		m = len(self.data)
		
		for i in range(m):
			estimatePrice = estimatePrice(self.theta0, self.theta1, self.scaledMileages[i])
			errors0.append(abs(estimatePrice - self.scaledMileages[i]))
			errors1.append(abs(estimatePrice - self.scaledMileages[i]) * self.dataPrices[i])
		return sum(errors0) / m, sum(errors1) / m

	def gradientDescent(self, alpha: float):
		epochs = 500
		for i in range(epochs):
			mae0, mae1 = self.lossFunction()
			self.theta0 -= alpha * mae0
			self.theta1 -= alpha * mae1
		print(self.theta0, self.theta1)


	def linearRegression(data):
		mileage = input("Mileage: ")
		try:
			mileage = float(mileage)
		except ValueError:
			print("Type Error")
			exit(1)
		theta = [data['km'][0], data['price'][0]]
		price = theta[0] + (theta[1] * mileage)
		print(f"estimatePrice({int(mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {mileage}) = {price:.2f}")
		# plt.show()
		return price

if __name__ == "__main__":
	linearRegression = LinearRegression()
	linearRegression.linearRegression()
	linearRegression.gradientDescent(0.5)

