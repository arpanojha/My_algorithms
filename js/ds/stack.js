class Node{
  constructor(val){
    this.val=val
    this.next = null
  }
}

class Stack{
  constructor(){
    this.first=null
    this.last=null
    this.length=0
  }
  push(val){
    var newNode = new Node(val)
    if(this.first===null){
      this.first = newNode
      this.last = newNode
      this.length++
      return this
    }
    newNode.next = this.first
    this.first = newNode
    this.length++
    return this
  }
  pop(){
    if(this.first===null){
      return undefined
    }
    if(this.first===this.last){
      console.log(`Popping ${this.first.val}`)
      this.first=null
      this.last=null
      return undefined
    }
    console.log(`Popping ${this.first.val}`)
    this.first = this.first.next
    this.length--
    return this
  }
}

var s = new Stack()
s.push('s')
s.push('t')
s.push('a')
s.pop()
s.pop()
s.pop()
