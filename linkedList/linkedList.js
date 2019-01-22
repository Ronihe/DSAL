//node class, each node has a value and has a pointer to the next
class Node {
  constructor(val) {
    this.value = val;
    this.next = null;
  }
}

class linkList {
  constructor(val) {
    this.head = null;
    (this.tail = null), (this.length = 0);
  }

  // Insert
  // push , add a new node to the end of the linked List
  //1. accpet a value, create a new code and pass it here
  // if there is no head, set head and tail to be the newly create node
  // otherwise set the next property of the tail to be the new node to be the newly created one
  // increment the length by one

  push(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  // remove
  // pop: remove the node from the end
  // if the lst is empty, return undefined
  // loop through the list get the previous node for tail and make it the new tail
  //decrement the length by 1

  pop() {
    if (!this.head) return undefined;
    let current = this.head;
    let newTail = current;
    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    this.tail.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return this;
  }

  //shift: remove the new noe from the beginning of the linked list
  // if there is not nodes, return undefined
  //store the current head property in a varaible;
  // get the head.next, set the head.next as the new head,
  // decrement the length by one
  shift() {
    if (!this.head) return undefined;
    this.head = this.head.next;
    this.length--;
    return this;
  }
  //unshift: accept a value and set it as the new head
  // create a new node and pass it to the function
  // if there is no head property on the list. set the head and tail to the property and length to be one
  unshift(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      this.length = 1;
    }
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  // get : accept an index
  // if the index is <0 or >=this.length, return null
  //loop through the list until you reach the index and reutnr the node
  get(idx) {
    if (idx < 0 || idx >= this.length) return null;
    let node = this.head;
    for (let i = 0; i < idx; i++) {
      node = node.next;
    }
    return node;
  }
  //set change the value of a node base on its position
  // accept an idex and a value
  //use the get() function getting the node and change the value
  // if
  set(idx, value) {
    if (!this.get(idx)) return false;
    this.get(idx).value = value;
    return true;
  }

  //insert: adding a node to the link at a specific postion
  //if the index is <0 || >=length,return false
  // find before and afer and create the link
  //if the index is the same as the length, just use push()
  // otherwise use the preNode = get(index-1)
  // set the newNode.next=preNode.next
  // set the preNode.next=newNode
  insert(idx, value) {
    if (idx < 0 || idx > this.length) return false;
    if (idx === this.length) {
      this.push(value);
      return true;
    }
    if (idx === 0) {
      this.shift(value);
      return true;
    }

    // if(index < 0 || index > this.length) return false;
    // if(index === this.length) return !!this.push(val);
    // if(index === 0) return !!this.unshift(val);
    const newNode = new Node(val);
    newNode.next = get(idx - 1).next;
    get(idx).next = newNode;
    this.length++;
    return true;
  }

  //remove accept a idx,
  // if idx <0 and > length, return false
  //if idx===length, pop
  // if idx ===0 , unshift
  // get(idx-1).next = get(idx).next

  //reverse
}

const testLinkedList = new linkList();
testLinkedList.push('andrew');
testLinkedList.push('roni');
testLinkedList.push('andrew');
console.log(testLinkedList);
testLinkedList.shift();
console.log('shifted', testLinkedList);
console.log(testLinkedList.get(0));
console.log(testLinkedList.set(1, 'anything'));
console.log(testLinkedList);
