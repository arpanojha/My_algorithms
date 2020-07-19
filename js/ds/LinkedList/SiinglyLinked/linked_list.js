class Node{
  constructor(val){
    this.val = val
    this.next=null
  }
}

class SinglyLinkedList{
  constructor(){
    this.head=null
    this.tail=null
    this.length=0
  }
  push(val){
    let newNode = new Node(val)
    if(this.head === null){
      this.head = newNode
      this.tail = newNode
    }else{
      this.tail.next = newNode
      this.tail = newNode
    }
    this.length++
    return this
  }
  traverse(){
    var inst = this.head
    while(inst){
      console.log(inst.val)
      inst = inst.next
    }
  }
  pop(){
    console.log(`Popping ${this.tail.val}`)
    var inst = this.head
    if(this.head === this.tail){
      this.head=null
      this.tail=null
      return undefined
    }
    while(inst){
      if(inst.next==this.tail)break
      inst = inst.next
    }
    this.tail=inst
    this.tail.next = null
    this.length--
    return this
  }
  shift(){
    if(this.head===null)return undefined
    if(this.head === this.tail){
      this.head=null
      this.tail=null
      return undefined
    }
    console.log(`Shifting ${this.head.val}`)
    this.head = this.head.next
    this.length--
    return this
  }
  unshift(val){
    var newNode = new Node(val)
    if(this.head===null){
      this.push(val)
      return this
    }
    newNode.next= this.head
    this.head = newNode
    this.length++
    return this
  }
  get(pos){
    if(pos>this.length-1||pos<0){
      console.log(`Pipe down your exitment . too optimistic number`)
      return null
    }
    var i=0
    var m = this.head
    while(i<this.length){
      if(i===pos){
        console.log(`Value at ${pos} is ${m.val}`)
        return m
      }
      m=m.next
      i++
    }
  }
  set(pos,val){
    var newNode = this.get(pos)
    if(newNode){
      newNode.val = val
      return true
    }
    return false
  }
  insert(pos,val){
    if(this.head===this.tail){
      this.push(val)
      return this
    }
    if(pos>=this.length){
      this.push(val)
      return this
    }
    if(pos<=0){
      this.unshift(val)
      return this
    }
    var newNode = new Node(val)
    var i=0
    var m = this.head
    while(i<this.length){
      if(i===pos-1){
        newNode.next=m.next
        m.next = newNode
        this.length++
        return this
      }
      m=m.next
      i++
    }
  }
  remove(pos){
    if(this.length===0){
      return undefined
    }
    if(this.length===1){
      return
    }
    if(pos>this.length-1||pos<0){
      console.log(`Clear your head , Have a walk and come back`)
      return null
    }
    if(pos===this.length-1){
      this.pop()
      return this
    }
    if(pos===0){
      this.shift()
      return this
    }
    var m = this.get(pos-1)
    m.next = m.next.next
    this.length--
    return this
  }
  reverse(){
    var m = this.head
    var n = this.head.next
    this.tail = m
    m.next=null
    while(n){
      var tmp = n.next
      n.next=m
      m=n
      n=tmp
    }
    this.head = m
    return this
  }
}


var v = new SinglyLinkedList()
v.push('a')
v.push('b')
v.push('c')
v.traverse()
v.pop()
v.traverse()
v.shift()
v.traverse()
v.unshift('m')
v.traverse()
v.push('n')
v.push('o')
v.push('p')
console.log('array')
v.traverse()
v.get(5)
console.log('Checking set')
v.set(4,'f')
v.traverse()
console.log("reverse")
v.reverse()
v.traverse()
console.log("reverse")
v.remove(2)
v.traverse()
