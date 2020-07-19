//insert===find === logn

class Node{
  constructor(val){
    this.val = val
    this.left = null
    this.right = null
  }
}

class Bst{
  constructor(){
    this.root=null
  }
  insert(val){
    var newNode = new Node(val)
    if(this.root===null){
      console.log(`root node ${val} !`)
      this.root = newNode
      return this
    }
    var m = this.root
    while(m){
      if(val===m.val){
        console.log(`duplicate entry ${val} not allowed`)
        return this
      }
      if(val>m.val){
        if(m.right===null){
          console.log(`inserting ${val} to right of ${m.val}`)
          m.right=newNode
          return this
        }
        m=m.right
      }
      if(val<m.val){
        if(m.left===null){
          console.log(`inserting ${val} to left of ${m.val}`)
          m.left=newNode
          return this
        }
        m=m.left
      }
    }
  }
  search(val){
    if(this.root===null){
      return undefined
    }
    if(this.root.val===val){
      console.log(`root node ${val} !`)
      return this
    }
    var m = this.root
    while(m){
      if(m.val ===val){
        console.log(`${val} is present`)
        return this
      }
      if(val>m.val){
        if(m.right===null){
          console.log(`${val} not found last searched at ${m.val}`)
          return this
        }
        m=m.right
      }
      if(val<m.val){
        if(m.left===null){
          console.log(`${val} not found last searched at ${m.val}`)
          return this
        }
        m=m.left
      }
    }
  }

}

var tr = new Bst()
tr.insert(10)
tr.insert(6)
tr.insert(15)
tr.insert(3)
tr.insert(8)
tr.insert(20)
tr.insert(15)
tr.insert(13)
tr.search(12)
