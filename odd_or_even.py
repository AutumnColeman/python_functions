# Write a function f(x) that returns 1 if x is odd and -1 if x is even. Plot it for x values of -5 to 5 in increments of 1. This time, instead of using plot.plot, use plot.bar

import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1


xs = range(-5, 5)
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()
