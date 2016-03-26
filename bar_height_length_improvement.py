from __future__ import division
from pylab import *
from numpy import *
from compartmentalize import compartmentalize
import sys

BIN_SIZE = 10
MAX_BIN_LENGTH = 200
MAX_SEARCH_LENGTH = 1600
N = 1000

def average(l):
    """
    computes the average
    of a list l to the nearest
    whole number.
    """
    return int(round(sum(l) / len(l)))

def improvement(length):
    """
    This function evaluates the ratio of the badness (defined
    in this program as the height of the bar times the length
    of the bar) of regularly blocked data to the badness of
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
        average_length = average([comp[0][i + 1][0] - comp[0][i][0] for i in range(len(comp[0]) - 1)])
        total_dblocked_badness += sum([(comp[0][i][2] - comp[0][i][1]) * (comp[0][i + 1][0] - comp[0][i][0]) for i in range(len(comp[0]) - 1)])
        rbadness = 0
        for start in range(0, length, average_length):
            if start + average_length > length:
                start = start - average_length
            else:
                minimum = float("inf")
                maximum = float("-inf")
                for pos in range(start, start + average_length):
                    minimum = min(minimum, dat[pos])
                    maximum = max(maximum, dat[pos])
                rbadness += (maximum - minimum) * average_length
        total_rblocked_badness += rbadness * length / (start + average_length)
    return total_rblocked_badness / total_dblocked_badness

def main():
    """
    This function evaluates improvement
    for various lengths.
    """
    out = open("bar_improvements_out.txt", "w")
    out.write("") #Clear the file.
    out.close()
    lengths = []
    improvements = []
    for length in range(BIN_SIZE, MAX_SEARCH_LENGTH, BIN_SIZE):
        imp = improvement(length)
        lengths.append(length)
        improvements.append(imp)
        print length, imp
        out = open("bar_improvements_out.txt", "a")
        out.write(str(length) + " " + str(imp) + "\n")
        out.close()
    plot(lengths, improvements)
    savefig("bar_improvements.png")
    show()

if __name__=="__main__":
    main()
