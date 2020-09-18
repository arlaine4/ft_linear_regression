import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#------------------------------------------#
# Initialisation du parseur d'arguments
#------------------------------------------#

parser = argparse.ArgumentParser(
	description="Predict a car's value using linear regression.")
parser.add_argument('kms', help="car's mileage")
parser.add_argument('--graph', '-g', action='store_true', help='show graph')
options = parser.parse_args()

#------------------------------------------#

def predict_car_price(theta0, theta1, km):
	"""Prediction du prix du vehicule a partir
	des thetas et du kilometrage donnee
	en parametre"""
	return theta0 + theta1 * km

if __name__ == "__main__":
	try:
		thetas = pd.read_csv("thetas.csv")
		theta0 = thetas.at[0, 'theta0']
		theta1 = thetas.at[0, 'theta1']
	except:
		print("Error with the csv for thetas.")
		exit()
	if options.graph:
		#---------------------------------------#
		# Si option graph, preparation donnees
		# pour tracer du graph
		#---------------------------------------#
		try:
			data = pd.read_csv("data.csv")
			X = data['km'].values
			Y = data['price'].values
			line = theta0 + theta1 * X
		except:
			print("Error with the csv file.")
			exit(1)
		#---------------------------------------#
	predicted_price = predict_car_price(theta0, theta1, int(options.kms))
	print("The price for a car with {} km is estimated at {}".format(options.kms, round(predicted_price)))
	if options.graph:
		#-----------------------------------------------------#
		# Si l'argument de graph est renseigne, on affiche le
		# graph avec matplotlib.pyplot
		#-----------------------------------------------------#
		axes = plt.axes()
		axes.grid()
		plt.scatter(X, Y)
		plt.plot(X, line, c='g')
		plt.title('Estimated price for {} Km'.format(options.kms))
		plt.show()
		#-----------------------------------------------------#
	
	
