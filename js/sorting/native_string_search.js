
d=[]
function native_string_search(a,b){
//  console.log(a.length,b.length)
  for(var i=0;i<=(a.length-b.length);i++){
    for(var j=0;j<b.length;j++){
      //console.log(a[i+j],b[j])
      if(b[j]!==a[i+j]){
      //  console.log("break")
        break;
      }
      if(j===b.length-1){
        d.push(i)
      }
    }
  }
  return d
}

console.log(native_string_search('wowomgzomg','omg'))
