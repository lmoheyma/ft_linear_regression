from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt
import time

class LinearRegression:
	def __init__(self) -> None:
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


	def denormalizeData(self, t0, t1):
			minM = self.dataMileages.min()
			maxM = self.dataMileages.max()
			minP = self.dataPrices.min()
			maxP = self.dataPrices.max()
			return t0 * (maxP - minP) + minP + (t1 * minM * (minP - maxP)) / (maxM - minM), t1 * (maxP - minP) / (maxM - minM)
			


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
		plt.title("Plot")
		i=0

		m = len(self.data)

		price0 = self.estimatePrice(self.theta0, self.theta1, 0)
		price1 = self.estimatePrice(self.theta0, self.theta1, 1)
		lin_reg = plt.plot([0, 1], [price0, price1], color='red')
		plt.ion()

		figure, ax = plt.subplots(figsize=(10, 8))
		line1, = ax.plot(price0, price1)

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
			line1.set_xdata([price0])
			line1.set_ydata([price1])

			figure.canvas.draw()

			figure.canvas.flush_events()
 
			# time.sleep(0.1)
    		# plt.pause(1e-10)


		print(self.theta0, self.theta1)
		




	def linearRegression(self):
		mileage = input("Mileage: ")
		try:
			mileage = float(mileage)
		except ValueError:
			print("Type Error")
			exit(1)
		theta = [self.data['km'][0], self.data['price'][0]]
		price = theta[0] + (theta[1] * mileage)
		print(f"estimatePrice({int(mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {mileage}) = {price:.2f}")
		# plt.show()
		return price

if __name__ == "__main__":
	linearRegression = LinearRegression()
	linearRegression.linearRegression()
	linearRegression.gradientDescent(0.1)

