from __future__ import division
import sys
sys.path.insert(0, "../Bins")
import compartmentalize
from pylab import *
from numpy import *

a = random.rand(1000)
print a
print compartmentalize.compartmentalize(a)
