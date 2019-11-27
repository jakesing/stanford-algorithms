console.time("total")

function mergeSort(arr){
    let arrLen = arr.length;
    if(arrLen <= 1){
        return arr;
    }
    let left = arr.slice(0,Math.floor(arr.length/2))
    let right = arr.slice(Math.floor(arr.length/2), arr.length)
    console.log(arr.length / 2)
    console.log("Right copy: " + right);
    
    //sort first half of input 
    left = mergeSort(left);
    right = mergeSort(right);
    
    return merge(left,right)
}

function merge(a,b){
    let aLen = a.length
    let bLen = b.length

    let output = []
    let indexLeft = 0;
    let indexRight = 0;



    while(indexLeft < aLen && indexRight < bLen){
        if(a[indexLeft] < b[indexRight]){
            output.push(a[indexLeft]);
            indexLeft++;
        }
        else{
            output.push(b[indexRight])
            indexRight ++ ;
        }
    }
    
    return output.concat(a.slice(indexLeft)).concat(b.slice(indexRight))
}



let input = [2,5,3,4,7,1,100]

console.log(mergeSort(input));
console.timeEnd("total");
