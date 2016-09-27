import matplotlib.pyplot as plot
celcius = float(raw_input("Temperature in C? " ))

def fahrenheit(celcius):
    return (celcius * 1.8) + 32.0

xs = range(-10, 40)
ys = []
for x in xs:
    ys.append(fahrenheit(x))

plot.plot(xs, ys)
plot.show()
