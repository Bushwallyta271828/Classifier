from __future__ import division
from compartmentalize import compartmentalize
from pylab import *
import numpy as np

def comp_to_slices(compartmentalization):
    slices = []
    index = 0
    for i in range(0, 1000, 100):
        minimum = index
        maximum = len(compartmentalization) - 1
        while maximum - minimum > 1:
            middle = (maximum + minimum) // 2
            if compartmentalization[middle][0] < i:
                minimum = middle
            else:
                maximum = middle
        b = compartmentalization[minimum]
        slices.append((b[1], b[2]))
        index = minimum
    return slices

#def gen_exo():
    

def gen_nox():
    overall_lambda = 200 * np.random.random() + 400
    data = [[], [], [], [], []]
    for i in range(1000):
        overall = np.random.poisson(overall_lambda)
        for o in range(5):
            extra = np.random.poisson(500)
#            changing 
            data[o].append(extra)
    #dat = [np.random.poisson(900 * np.random.random() + 100,1000) * (1 + 0.1 * sin(random for i in range(5)] #Note: to be made slightly more "wavy" with extra product.
    return data

if __name__=="__main__":
    data = gen_nox()
    for o in range(5):
        plot(data[o])
    show()
