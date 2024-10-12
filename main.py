from leastSquareEstimation import estimatePrice
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
	theta = [data['km'][0], data['price'][0]]
	price = theta[0] + (theta[1] * mileage)
	print(f"estimatePrice({int(mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {mileage}) = {price:.2f}")
	# plt.show()
	return 0

if __name__ == "__main__":
	main()