from leastSquareEstimation import predictPrice
from load_csv import load
import pandas as pd

def main():
	data = load("data.csv")
	theta = predictPrice(data)
	mileage = input("Mileage: ")
	try:
		mileage = float(mileage)
	except ValueError:
		print("Type Error")
		exit(1)
	estimatePrice = theta[0] + (theta[1] * mileage)
	print(f"estimatePrice({mileage}) = {theta[0]:2f} + ({theta[1]:2f} ∗ {mileage}) = {estimatePrice:2f}")
	return 0

if __name__ == "__main__":
	main()