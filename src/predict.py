import json

def loadThetas():
	try:
		with open('thetas.json', 'r') as outfile:
			return json.load(outfile)
	except Exception:
		print("File Error: Can't save thetas")
		exit(1)

def predictPrice():
	mileage = input("Mileage: ")
	try:
		mileage = float(mileage)
	except ValueError:
		print("Type Error")
		exit(1)
	data = loadThetas()
	theta = [data['theta0'], data['theta1']]
	print(theta)
	price = theta[0] + (theta[1] * mileage)
	print(f"estimatePrice({int(mileage)}) = {theta[0]:.2f} + ({theta[1]:.2f} ∗ {mileage}) = {price:.2f}")

if __name__ == "__main__":
	predictPrice()