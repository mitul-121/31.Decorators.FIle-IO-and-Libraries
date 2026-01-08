import numpy

file = numpy.loadtxt('random_number.csv', delimiter=',')

mean = numpy.mean(file)
median = numpy.median(file)
mode = numpy.mod(file, 2)

print(mean)
print(median)
print(mode)



