import scipy.integrate as integrate #Scipy is only used to avoid hardcoding the known value of the integral
import matplotlib.pyplot as plt

#numerical integration via Riemann sum


#func: lambda ___ function to be integrated
#a, b: float  ___ lower and upper bound
#bins: int    ___ number of subdivisions
#mode: string ___ point of evaluation ('left', 'mid', 'right')
def riemann(func, a, b, numBins=10000, mode='mid'):
    step = (b-a) / numBins
    
    if mode == 'left':
        bins = [(a + i*step) for i in range(numBins)]
    elif mode == 'mid':
        bins = [(a + (i+1/2)*step) for i in range(numBins)]
    elif mode == 'right':
        bins = [(a + (i+1)*step) for i in range(numBins)]
    else:
        print("Invalid mode for function 'riemann': " + mode)

    total = sum([func(x)*step for x in bins])
    return total


#plot convergence speed for left, midpoint, and right Riemann sums
#binrange: int tuple ___ provides range of subdivisions to evaluate
def plotRiemann(func, a, b, binRange=(10,220), numIntervals=40):
    known = integrate.quad(func, a, b)[0]
    left, mid, right = [], [], []
    step = int((binRange[1]-binRange[0]) / numIntervals)
    binNums = [round(binRange[0] + i*step) for i in range(numIntervals)]

    for num in binNums:
        left.append (abs(riemann(func, a, b, numBins=num, mode='left' ) - known))
        mid.append  (abs(riemann(func, a, b, numBins=num, mode='mid'  ) - known))
        right.append(abs(riemann(func, a, b, numBins=num, mode='right') - known))

    labels = ['Left', 'Midpoint', 'Right']
    plt.plot(binNums, left)
    plt.plot(binNums, mid)
    plt.plot(binNums, right)
    plt.title('Convergence of left, right, and midpoint Riemann sums')
    plt.xlabel('Number of bins')
    plt.ylabel('Absolute error')
    plt.legend(labels)
    plt.show()
        
        


if __name__ == '__main__':
    func = lambda x: 3*x*x*x - 4*x*x + 3.2198*x
    a,b = 1,9
    bins = 10000
    left  = riemann(func, a, b, numBins=bins, mode='left')
    mid   = riemann(func, a, b, numBins=bins, mode='mid')
    right = riemann(func, a, b, numBins=bins, mode='right')

    print("Integration of 3x^3 - 4x^2 + 3.2198x from 1 to 9")
    print("Riemann sum with {} bins\n\n".format(bins))
    print("Known: " + "4078.13")
    print("Left:  " + str(round(left, 2)))
    print("Mid:   " + str(round(mid, 2)))
    print("Right: " + str(round(right, 2)))

    plotRiemann(func, a, b)
