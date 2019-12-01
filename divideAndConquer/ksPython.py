test1 = 3141592653589793238462643383279502884197169399375105820974944592
test2 = 2718281828459045235360287471352662497757247093699959574966967627


def multiply(x, y):
    length = len(str(x))
    if length == 1:
        return int(x) * int(y)
    else:
        a = str(x)[0:length / 2]
        b = str(x)[length / 2:length]
        c = str(y)[0:length / 2]
        d = str(y)[length / 2:length]
        return (multiply(a, c) * (10**length)) + ((multiply(a, d) + multiply(b, c)) * (10 ** (length/2)) + multiply(b, d))


print(multiply(test1,test2))