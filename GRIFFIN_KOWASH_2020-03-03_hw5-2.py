#simple list sorting function


#Orders the provided list from smallest to largest.
#For each value in the provided array, first compare it to the largest element
#in the ordered list, and append if it's larger. Otherwise, search through the
#list until its proper place is found and insert it.
def sort(vals):
    ordered = [vals[0]] #initialize with first element
    for valToSort in vals[1:]:
        if valToSort >= ordered[-1]:
            ordered.append(valToSort)
        else:
            for i, checkVal in enumerate(ordered):
                done = False
                if valToSort <= checkVal:
                    ordered.insert(i, valToSort)
                    break
    return ordered


if __name__ == '__main__':
    test = [4,5,5,1,96,2,1,12,28,11]
    print(test)
    print(sort(test))
