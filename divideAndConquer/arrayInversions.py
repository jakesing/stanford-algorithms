from mergeSort import *



# Inversions: number of pairs (i,j) of array (A) indices with i<j and A[i] > A[j]
# n(n-1) / 2 -- the max number of inversions in an array of length n


# brute force algorithm - full looping
'''
for i in range(len(testArray)):
    for j in range(1, len(testArray)):
        if (i < j) and (testArray[i] > testArray[j]):
            count += 1;
'''

# call the merge sort function, which has been modified to count the split inversions.
file = "IntegerArray.txt"

def alg(filePath):
    splitInv.count = 0
    ourArray = []
    file = open(filePath, "r")
    for line in file:
        ourArray.append(int(line))

    merge_sort(ourArray)
    return splitInv.count

print alg(file)