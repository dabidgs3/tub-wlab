#!/usr/bin/python -tt
# Python Interpreter: 3.4.1
# # Import Built-In Libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab

y = [-10.1, -1.2,-9.5,-1,-1,-1,0.1, 5, 7, 7, 7, 7, 2, 2, 2]
x = [ i for i in range(0, len(y))]
print x
ys = sorted(y)
print ys
print np.median(y)
print reduce(lambda a, b: a + b, y) / len(y)

#CDF
#cumulative = np.cumsum(ys)
yvals=np.arange(len(ys))/float(len(ys)-1)
plt.figure(1)
plt.bar(ys,yvals,color='r')
plt.title('CDF')
plt.xlabel('Data set [x]')
plt.ylabel('P(x)')
plt.savefig('images/cdf.eps', format='eps', dpi=1000)
#plt.show()

plt.figure(2)
plt.bar(x,y,color='b')
plt.title('Printed Data set')
plt.xlabel('x')
plt.ylabel('Data Set Values')
#plt.legend((x,y),('Vector[x]','Values'))
#Saves the file with eps format
plt.savefig('images/ecdf.eps', format='eps', dpi=1000)

#BoxPlot
plt.figure(3)
plt.boxplot(y,notch=1)
plt.title('Box Plot for Median')
plt.xlabel('Data set [x]')
plt.ylabel('Confidence Interval')
plt.savefig('images/boxplot.eps', format='eps', dpi=1000)

#QQplot
plt.figure(4)
stats.probplot(y, dist="norm", plot=pylab)
pylab.savefig('images/qqplot.eps', format='eps', dpi=1000)

#SMA
N=len(y)
cumsum = np.cumsum(np.insert(y, 0, 0))
print (cumsum[N:] - cumsum[:-N]) / N
#pylab.show()
#plt.show()
