//Complexity is n^2

function bubbleSort(a){
  for(var i=0;i<a.length;i++){
    var count=0
    for(var j=0;j<a.length-1;j++){
      if(a[j]>a[j+1]){
        a[j]=a[j]+a[j+1]
        a[j+1]=a[j]-a[j+1]
        a[j]= a[j]-a[j+1]
        count++
      }
    }
    if(count==0){
      return a
    }
  }
  return a

}


console.log(bubbleSort([6,5,7,8,4,2,3,1]))
