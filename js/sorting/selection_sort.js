//complexity n^2

function selectionSort(a){
  for(var i=0;i<a.length;i++){
    var min = i
    for(var j=i+1;j<a.length;j++){
      if(a[j]<a[min]){
        min = j
      }
    }
    if(i!==min){
      a[min]=a[i]+a[min]
      a[i]=a[min]-a[i]
      a[min]= a[min]-a[i]
    }
  }
  return a
}

console.log(selectionSort([6,5,7,8,4,2,3,1]))
