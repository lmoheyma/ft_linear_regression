from leastSquareEstimation import predictPrice
from load_csv import load
from matplotlib import pyplot as plt

def main():
	data = load("data.csv")
	mileage = input("Mileage: ")
	try:
		mileage = float(mileage)
	except ValueError:
		print("Type Error")
		exit(1)
	theta = predictPrice(data)
	estimatePrice = theta[0] + (theta[1] * mileage)
	print(f"estimatePrice({mileage}) = {theta[0]:2f} + ({theta[1]:2f} ∗ {mileage}) = {estimatePrice:2f}")
	plt.show()
	return 0

if __name__ == "__main__":
	main()