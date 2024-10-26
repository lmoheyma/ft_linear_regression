from load_csv import load

def estimatePrice():
	mileage = input("Mileage: ")
	try:
		mileage = float(mileage)
	except ValueError:
		print("Type Error")
		exit(1)
	data = load("data.csv")
	theta = [data['km'][0], data['price'][0]]
	price = theta[0] + (theta[1] * mileage)
	print(f"estimatePrice({int(mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {mileage}) = {price:.2f}")
	return price

if __name__ == "__main__":
	estimatePrice()