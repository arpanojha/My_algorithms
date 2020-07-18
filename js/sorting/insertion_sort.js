//n^2 complexity

function insertionSort(a){
  for(var i=1;i<a.length;i++){
    var temp = a[i]
    for(var j=i-1;j>=0;j--){
      if(a[j]>temp){
        a[j+1]=a[j]
      }else{
        break
      }
      }
      a[j+1]=temp
    }
    return a
  }
console.log(insertionSort([6,5,7,8,4,2,3,1]))


5,6,7,8,4,3,2,1
