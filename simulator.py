from __future__ import division
from compartmentalize import compartmentalize
from pylab import *
import numpy as np

#def gen_exo():
    

def gen_nox():
    dat = np.random.poisson(900 * np.random.random() + 100,1000) #Note: to be made slightly more "wavy" with extra product.
    comp = compartmentalize(dat)[0]
    for inum, i in enumerate(comp[:-1]):
        n = comp[inum + 1]
        plot([i[0], n[0] - 1], [i[1], i[1]], "green")
        plot([i[0], n[0] - 1], [i[2], i[2]], "red")
    plot(dat, "blue")
    show()

if __name__=="__main__":
    gen_nox()

#a = [50*random() - 100 * 2.71828**(-(i / 50 - 2)**2) for i in range(200)]
#comp = compartmentalize(a)[0]
#for inum, i in enumerate(comp[:-1]):
#    n = comp[inum + 1]
#    sl = a[i:n]
#    largest = max(sl)
#    smallest = min(sl)
#    plot([i, n], [largest, largest], "red")
#    plot([i, n], [smallest, smallest], "green")
#plot(range(200), a, "blue")
#show()
