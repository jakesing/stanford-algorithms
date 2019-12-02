from mergeSort import merge_sort

# Inversions: number of pairs (i,j) of array (A) indices with i<j and A[i] > A[j]
# n(n-1) / 2 -- the max number of inversions in an array of length n

testArray = [1, 3, 5, 2, 4, 6,0,100]

count = 0

# brute force algorithm - full looping
for i in range(len(testArray)):
    for j in range(1, len(testArray)):
        if (i < j) and (testArray[i] > testArray[j]):
            count += 1;




# inversion with recursion - left inversion if i & j <= n/2, call it a right inversion if i & j are both > n/2
# split inversion if i <= n/2 < j -we'll recursively calculate all of these and return the sum
# also the base case - if len of array is 1, return 0


# have recursive calls both count inversions AND sort using merge sort

print(merge_sort(testArray))