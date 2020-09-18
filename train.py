import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def	read_inside_data(data):
	"""Recuperation dans l'echantillon de donnees et stockage
	dans des matrices"""
	X = np.array(data['km'].values)
	X_old = X
	X = scaling_data(X, max(X))
	X = np.c_[np.ones(X.shape[0]), X]
	Y = np.array(data['price'].values)
	Y_old = Y
	Y = scaling_data(Y, max(Y))
	return X, Y, X_old, Y_old

def	scaling_data(data, scale):
	"""Scaling des data"""
	return data / scale

def	thetas_csv(thetas):
	"""Enregistrement des thetas dans le csv"""
	with open("thetas.csv", "r+") as fd:
		data = str(thetas[0]) + ',' + str(thetas[1]) + '\n'
		newdata = ",theta0,theta1\n0," + data
		fd.write(newdata)

def	linear_regression_thetas(thetas, X, Y, learning_rate, m):
	"""Loop de regression lineaire"""
	while 1:
		old_thetas = thetas
		thetas = thetas - learning_rate * (1 / m) * (X.T @ ((X @ thetas) - Y))
		if np.array_equal(thetas, old_thetas):
			break
	return thetas

def	calcul_thetas(X, Y, X_old, Y_old, learning_rate):
	"""Fonction de calcul des thetas pour enregistrer dans le csv
	et l'utiliser dans le programe de prediction du prix d'une voiture"""
	#Learning_rate defined in call function in main, its value is 1
	m = float(len(X))
	thetas = np.array([0,0])
	thetas = linear_regression_thetas(thetas, X, Y, learning_rate, m)
	thetas[0] = thetas[0] * max(Y_old)
	thetas[1] = thetas[1] * (max(Y_old) / max(X_old))
	return thetas

if __name__ == "__main__":
	try:
		data = pd.read_csv("data.csv")
		X, Y, X_old, Y_old = read_inside_data(data)
	except:
		print("Error with data.csv, stopping now.")
		exit()
	thetas = calcul_thetas(X, Y, X_old, Y_old, 1)
	thetas_csv(thetas)
	#---------------------------#
	# Graph regression lineaire
	#---------------------------#
	line = thetas[0] + thetas[1] * X_old
	plt.scatter(data['km'].values, data['price'].values)
	plt.plot(X_old,line, c='r')
	plt.title('Estimation prix')
	plt.xlabel('Kilometrage')
	plt.ylabel('Prix')
	plt.show()
	#---------------------------#
