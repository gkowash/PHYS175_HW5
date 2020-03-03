import matplotlib.pyplot as plt

#finding linear correlation coefficient


#sqrt, mean, and stdDev copied from Problem 1

def sqrt(x, prec=0.0001, testMode=False):
    if x < 0:
        print("Input to function 'sqrt' must be a positive number.")
        return None
    guess = x/5
    error = x - guess*guess
    count = 0
    while abs(error) > prec:
        guess = guess + error/30 #not sure what this modification should be
        error = x - guess*guess
        count += 1
    if testMode:
        print("\n\nValue: "+str(x))
        print("Known: "+str(np.sqrt(x)))
        print("Guess: "+str(guess))
        print("Iterations: "+str(count))  
    return guess

def mean(y):
    return sum(y) / len(y)

def stdDev(y):
    sqDiffSum = 0
    avg = mean(y)
    for yi in y:
        sqDiffSum += (yi - avg)*(yi - avg)
    sqDiffAvg = sqDiffSum / len(y)
    return sqrt(sqDiffAvg)

def testRoot():
    root0 = sqrt(4, testMode=True)
    root1 = sqrt(49, testMode=True)
    root2 = sqrt(1.46, testMode=True)
    root3 = sqrt(6.77, testMode=True)
    root4 = sqrt(0.2275, testMode=True)
    print('\n\n\n')



def linearCorr(x, y, bins=10, plotting=False):
    xy = [xi*yi for xi,yi in zip(x,y)]
    Exy = mean(xy)
    ux = mean(x)
    uy = mean(y)
    sx = stdDev(x)
    sy = stdDev(y)
    Vxy = Exy - ux*uy
    
    rho = Vxy / (sx*sy)

    if plotting:
        plt.hist2d(x, y, bins=bins)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Histogram showing correlation between x and y')
        plt.show()

    return rho



if __name__ == '__main__':
    file = open('random_x_y_pairs.txt','r')
    lines = file.readlines()
    file.close()

    x = []
    y = []
    for line in lines:
        xStr, yStr = line.split()
        x.append(float(xStr))
        y.append(float(yStr))

    rho = linearCorr(x, y, bins=25, plotting=True)
    print('Correlation coefficient: ' + str(rho))
    
