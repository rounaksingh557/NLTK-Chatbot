from predict_response import startPredict
from train_bot import train

if __name__ == "__main__":
    ask = input("Have you trained your model (y/n): ")
    if ask == "y":
        startPredict()
    elif ask == "n":
        train()