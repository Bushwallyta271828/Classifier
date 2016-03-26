from __future__ import division
from pylab import *
from numpy import *
from compartmentalize import compartmentalize
import sys

BIN_SIZE = 10
MAX_BIN_LENGTH = 200
MAX_SEARCH_LENGTH = 1600
N = 1000
f = open("xis.txt")
flines = f.readlines()
f.close()
barmap = [None, None]
for fline in flines:
    xi = float(fline[:-1].split(":")[1])
    barmap.append(xi)

def average(l):
    return sum(l) / len(l)

def improvement(length):
    """
    This function evaluates the ratio of the badness
    of regularly blocked data to the badness of 
    dynamically blocked data on randomly generated data
    of given length.
    "rblocked" stands for "regularly blocked"
    "dblocked" stands for "dynamically blocked"
    """
    total_rblocked_badness = 0
    total_dblocked_badness = 0
    for i in range(N):
        dat = [normal() + 2*sin(j / 25) for j in range(length)]
        comp = compartmentalize(dat, max_length=MAX_BIN_LENGTH, max_pval=2.0/BIN_SIZE)
        average_length = <blah>
        total_dblocked_badness += comp[1]
        rbadness = 0
        for start in range(0, length, average_length):
            minimum = float("inf")
            maximum = float("-inf")
            for pos in range(start, start + BIN_SIZE):
                if dat[pos] < minimum:
                    minimum = dat[pos]
                if dat[pos] > maximum:
                    maximum = dat[pos]
            rbadness += (maximum - minimum) * barmap[BIN_SIZE]
        total_rblocked_badness += rbadness
    return total_rblocked_badness / total_dblocked_badness

def main():
    """
    This function evaluates improvement
    for various lengths.
    """
    out = open("fair_improvements_out.txt", "w")
    out.write("") #Clear the file.
    out.close()
    lengths = []
    improvements = []
    for length in range(BIN_SIZE, MAX_SEARCH_LENGTH, BIN_SIZE):
        imp = improvement(length)
        lengths.append(length)
        improvements.append(imp)
        print length, imp
        out = open("fair_improvements_out.txt", "a")
        out.write(str(length) + " " + str(imp) + "\n")
        out.close()
    plot(lengths, improvements)
    savefig("fair_improvements.png")
    show()

if __name__=="__main__":
    main()
