
exList = [5,2,3,7,8,9,4,5,6,1,0,3,5]

import statistics as s
print(s.mean(exList))
print(s.median(exList))
print(s.mode(exList))
print(s.stdev(exList))
print(s.variance(exList))

from statistics import mean
print(mean(exList))

from statistics import mean as m
print(m(exList))

from statistics import mean, stdev
print(mean(exList), stdev(exList))

from statistics import mean as m, stdev as sd
print(m(exList), sd(exList))

from statistics import *
print(mean(exList), stdev(exList))