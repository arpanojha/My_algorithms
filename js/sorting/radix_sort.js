
function getDigit(n,d){
  return (n%Math.pow(10,d+1)-(n%Math.pow(10,d)))/Math.pow(10,d)
}
function getdigitByMod(n,d){
  return Math.floor(Math.abs(n)/Math.pow(10,d))%10
}
function digitCount(n){
  return n.toString().length
}
function digitCountByMath(n){
  if(n===0){
    return 0
  }
  return Math.floor(Math.log10(Math.abs(n)))+1
}
function maxDigits(a){
  let c = 0
  for(v in a){
    if(c<digitCount(a[v])){
      c = digitCount(a[v])
    }
  }
  return c
}
function radixSort(a){
  let maxdigits = maxDigits(a)
  for(var i=0;i<maxdigits;i++){
    let bucket = Array.from({length :10}, () => [])
    for(let k=0;k<a.length;k++){
      bucket[getDigit(a[k],i)].push(a[k])
    }
    a = [].concat(...bucket)
  }
  return a

}

console.log(radixSort([]))
console.log(getdigitByMod(12345,3))
console.log(digitCountByMath(12345))
console.log(radixSort([23,345,5467,12,2345,9852]))
