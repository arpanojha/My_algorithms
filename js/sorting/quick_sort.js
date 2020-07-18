//n*logn  worst n^2

function quickSort(a,i=0,j=a.length-1){
  if(i<j){
  let ind = pivot(a,i,j)
  quickSort(a,i,ind-1)
  quickSort(a,ind+1,j)}
  return a
}
function pivot(a,i=0,j=a.length-1){
  var pivot = a[i]
  var cur = i
  for(var n = i+1;n<=j;n++){
    if(pivot>a[n]){
      cur++
      var tmp = a[n]
      a[n]=a[cur]
      a[cur]=tmp
    }
  }
  var tmp1 = a[cur]
  a[cur] = a[i]
  a[i] = tmp1
  //console.log(a)
  return cur
}

console.log(quickSort([4,8,2,1,5,7,6,3]))
