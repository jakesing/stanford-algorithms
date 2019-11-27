function multiply(x, y){
    let xLen = x.toString().length

    //split the numbers into the component pieces - left half and right half of both the left half and the right half :) 
    let b = x % (10**(xLen/2));
    let a = (x - b)/(10**(xLen/2))
    let d = y % ((10**(xLen/2)));
    let c = (y - d)/(10**(xLen/2));
    // console.log([a,c],[a,d], [b,c], [b,d])
    // console.log(a*c,a*d,b*c, b*d)
    
    //recursion base case:
    if(xLen == 1){
        return x*y;
    }
    //recursive call to calculate the Karatsuba product:
    else{
        return (multiply(a,c)*(10**xLen))+((multiply(a,d)+multiply(b,c))*(10**(xLen/ 2)))+multiply(b,d)
    }
    

}

//tests
let test1 = 3141592653589793238462643383279502884197169399375105820974944592
let test2 = 2718281828459045235360287471352662497757247093699959574966967627
console.time("karatsuba")
let a = multiply(test1,test2)
console.log(a)
console.timeEnd("karatsuba");

console.time("native")
let b = test1*test2
console.log(b)
console.timeEnd("native");

console.log(a == b)
