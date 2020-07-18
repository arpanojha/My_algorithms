// n*log(n)


function mergeArray(a,b){
  if(a[a.length-1]<b[0]){
    return a.concat(b)
  }
  if(b[b.length-1]<a[0]){
    return b.concat(a)
  }
  var d=[]
  var l = a.length+b.length
  var m=0
  var n=0
  for(var i=0;i<l;i++){
    if(m===a.length){
      d = d.concat(b.slice(n,b.length))
      break
    }
    if(n===b.length){
      d = d.concat(a.slice(m,a.length))
      break
    }
    if(a[m]<b[n]){
      d.push(a[m])
      m++
    }else{
      d.push(b[n])
      n++
    }
  }
  return d
}


function mergeSort(a){
  if(a.length<=1){
    return a
  }
  let mid = Math.floor(a.length/2)
  let left = mergeSort(a.slice(0,mid))
  let right = mergeSort(a.slice(mid))
  return mergeArray(left,right)
}

console.log(mergeArray([1,10,50],[2,14,99,100]))
console.log(mergeArray([1,2,3],[4,5,6]))
console.log(mergeSort([10,24,76,73,72,1,9]))
