import model_training
import sys

def predict_prize(km, theta_0, theta_1):
    km = int(km)
    estimated_prize = theta_0 + (theta_1 * km)
    print("Estimated prize for {} km is : {}".format(km, estimated_prize))

if __name__ == "__main__":
    theta_0, theta_1 = model_training.return_thetas()
    if len(sys.argv) == 3:
        predict_prize(sys.argv[1], theta_0, theta_1)
    elif len(sys.argv) < 3:
        print("Missing km to determine prize for the car.")
    elif len(sys.argv) > 3:
        print("Too many arguments.")
