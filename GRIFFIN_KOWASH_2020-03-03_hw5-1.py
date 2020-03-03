import numpy as np
import matplotlib.pyplot as plt


#very inefficient numerical square root. Works best with numbers below 100. 
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

    
if __name__ == "__main__":
    testRoot()

    testList = [2,3,4,2]
    print("___'Hipster' version of standard deviation function___\n\n")
    print(testList)
    print("\nStandard deviation")
    print("Known: " + str(np.std(testList)))
    print("Calculated: " + str(stdDev(testList)))
