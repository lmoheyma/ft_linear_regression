from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt
import json

class LinearRegression:
	def __init__(self) -> None:
		self.mileage = 0
		self.theta0 = 0.0
		self.theta1 = 0.0
		self.data = load("data.csv")
		self.dataMileages = self.data['km']
		self.dataPrices = self.data['price']
		self.normalizedData = self.normalizeData()


	def normalizeData(self):
		def normalizeSerie(serie: pd.core.frame.DataFrame):
			minimum = serie.min()
			return (serie - minimum) / (serie.max() - minimum)
		return pd.DataFrame({'km': normalizeSerie(self.dataMileages), 'price': normalizeSerie(self.dataPrices)})


	def denormalizeData(self):
		minM = self.dataMileages.min()
		maxM = self.dataMileages.max()
		minP = self.dataPrices.min()
		maxP = self.dataPrices.max()
		return self.theta0 * (maxP - minP) + minP + (self.theta1 * minM * (minP - maxP)) / (maxM - minM), self.theta1 * (maxP - minP) / (maxM - minM)
			

	def estimatePrice(self, theta0, theta1, mileage) -> float:
		try:
			mileage = float(mileage)
		except ValueError:
			print("Type Error")
			exit(1)
		return float(theta0 + (theta1 * mileage))


	def lossFunction(self):
		sumError0 = 0
		sumError1 = 0
		m = len(self.data)
		
		for i in range(m):
			estimatePrice = self.estimatePrice(self.theta0, self.theta1, self.normalizedData['km'][i])
			sumError0 += estimatePrice - self.normalizedData['price'][i]
			sumError1 += (estimatePrice - self.normalizedData['price'][i]) * self.normalizedData['km'][i]
		return sumError0, sumError1


	def gradientDescent(self, alpha: float):
		plt.scatter(self.normalizedData['km'], self.normalizedData['price'])
		plt.xlabel("Kilometers")
		plt.ylabel("Prices")
		plt.title("Linear Regression")
		i=0
		m = len(self.data)

		while(True):
			tmpTheta0 = self.theta0
			tmpTheta1 = self.theta1

			error0, error1 = self.lossFunction()
			self.theta0 -= alpha * 1 / m * error0
			self.theta1 -= alpha * 1 / m * error1
			
			if (i % 1000 == 0):
				print(f"Epoch: {int(i / 1000)}    |    Error: {error0:.2}")
			if (tmpTheta0 == self.theta0 and tmpTheta1 == self.theta1):
				break
			i+=1
		price0 = self.estimatePrice(self.theta0, self.theta1, 0)
		price1 = self.estimatePrice(self.theta0, self.theta1, 1)
		self.theta0, self.theta1 = self.denormalizeData()
		print(f"Price after training: {self.estimatePrice(self.theta0, self.theta1, self.mileage):.2f}")
		plt.plot([0, 1], [price0, price1], color='red')
		self.saveThetas()
		plt.show()
		

	def linearRegression(self):
		mileage = input("Mileage: ")
		try:
			self.mileage = float(mileage)
		except ValueError:
			print("Type Error")
			exit(1)
		theta = [self.data['km'][0], self.data['price'][0]]
		price = theta[0] + (theta[1] * self.mileage)
		print(f"estimatePrice({int(self.mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {self.mileage}) = {price:.2f}")
		return price
	

	def saveThetas(self):
		try:
			with open('thetas.json', 'w') as outfile:
				data = {
					"theta0": self.theta0,
					"theta1": self.theta1
				}
				json.dump(data, outfile)
		except Exception:
			print("File Error: Can't save thetas")

if __name__ == "__main__":
	linearRegression = LinearRegression()
	linearRegression.linearRegression()
	linearRegression.gradientDescent(0.1)
