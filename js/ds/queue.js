

class Node{
  constructor(val){
    this.val=val
    this.next = null
  }
}

class Queue{
  constructor(){
    this.first=null
    this.last = null
    this.length = 0
  }
  enqueue(val){
    var newNode = new Node(val)
    if(this.first === null){
      this.first=newNode
      this.last=newNode
      this.length++
      return this
    }
    this.last.next=newNode
    this.last = newNode
    this.length++
    return this
  }
  dequeue(){
    if(this.first===null)return undefined
    if(this.first===this.last){
      console.log(`Removing ${this.first.val}`)
      this.first=null
      this.last=null
      this.length=0
      return this
    }
    console.log(`Removing ${this.first.val}`)
    this.first=this.first.next
    this.length--
    return this
  }
}

var v = new Queue()
v.enqueue('s')
v.enqueue('t')
v.enqueue('a')
v.dequeue()
v.dequeue()
v.dequeue()
v.dequeue()
