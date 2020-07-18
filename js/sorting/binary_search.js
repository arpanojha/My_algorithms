

function bin_search(a,n,i=0,j=-100){
  if(j===-100){
    j=a.length
  }
  if(i>=j){
    return -1
  }

  var ind = i+ parseInt((j-i)/2)
  console.log(ind,i,j)
  var m = a[ind]
  if(m===n){
    return ind
  }
  else if(m>n){
    return bin_search(a,n,i,ind)
  }else{
    return bin_search(a,n,ind+1,j)
  }
}

console.log(bin_search([1,2,3,4,5],2))
console.log(bin_search([1,2,3,4,5],1))
console.log(bin_search([1,2,3,4,5],3))
console.log(bin_search([1,2,3,4,5],4))
