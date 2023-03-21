import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    sig = 1/( 1+ math.exp(-z))
    print(sig)

# calculate the output of the sigmoid for x with all three coefficients
sigmoid(x @ c1) # changing c1 -> c2 or c3 gives different values.