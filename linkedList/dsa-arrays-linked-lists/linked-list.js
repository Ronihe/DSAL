/** Node: node for a singly linked list. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** LinkedList: chained together nodes. */

class LinkedList {
  constructor(vals = []) {
    this.head = null;
    this.tail = null;
    this.length = 0;

    for (let val of vals) this.push(val);
  }

  /** push(val): add new value to end of list. */

  push(val) {
    // create a new node with the val, set the variable of newNode to the new Node
    // if there is no node in the linked List, set and head and tail to the new node
    //if there is node in the linked list, find the tail and this.tal.next = newNode, set the new tail to the newNode
    // increase the length by 1
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    }
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
  }

  /** unshift(val): add new value to start of list. */

  unshift(val) {
    // create a new node with the val, set the variable of newNode to the new Node
    // if there is no node in the linked List, set and head and tail to the new node
    //if there is node in the linked list, make the newNode.next to this.head, and set the head to the newNode
    // increase the length by 1

    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    }
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
  }

  /** pop(): return & remove last item. */

  pop() {
    //if there is no node in the list, just throw error 'errors! empty linked list'
    //if there is only one node in the linked list, set head and tail to null
    //if there is more than one node in the linked list, using the while loop find the node before the tail
    //create a currNode variable to find currNode.next=this.tail
    // decrease the length by 1

    if (!this.head) {
      throw 'errors! empty linked list';
    } else if (this.length === 1) {
      const oldTailVal = this.tail.val;
      this.head = null;
      this.tail = null;
      this.length--;
      return oldTailVal;
    } else if (this.length === 2) {
      const oldTailVal = this.tail.val;
      this.head.next = null;
      this.tail = this.head;
      this.length--;
      return oldTailVal;
    } else {
      const oldTailVal = this.tail.val;
      const oldLength = this.length;
      let currNode = this.head;
      let newLength = 0;
      while (newLength <= oldLength - 2) {
        currNode = currNode.next;
        console.log('this.current node', currNode);
        newLength++;
      }
      currNode.next = null;
      this.tail = currNode;
      this.length--;
      return this.tail.val;
    }
  }

  /** shift(): return & remove first item. */
  // if there is no node in the list, just throw error 'errors! empty linked list'
  // create a variable to hold the head's val
  // if there is only one set the head to null
  //
  shift() {
    if (!this.head) {
      throw 'errors! empty linked list';
    }
    const shiftedHead = this.head.val;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      const secondToHead = this.head.next;
      this.head = secondToHead;
    }
    this.length--;
    return shiftedHead;
  }

  /** getAt(idx): get val at idx. */
  // if idx is not a integer and postive, throw err

  getAt(idx) {
    if (!(Number.isInteger(idx) && idx >= 0 && idx <= this.length - 1)) {
      throw 'invalid index';
    }
    if (!this.head) {
      return null;
    }

    let currNode = this.head;
    for (let i = 0; i <= idx - 1; i++) {
      currNode = currNode.next;
    }
    return currNode.val;
  }

  /** setAt(idx, val): set val at idx to val */
  // if there is only one node in the linked list, set the head and tail to the new node
  //else use the for loop to find the node and set the val to the node
  setAt(idx, val) {
    if (!(Number.isInteger(idx) && idx >= 0 && idx <= this.length - 1)) {
      throw 'invalid index';
    }

    if (this.length === 1) {
      this.head.val = val;
      this.tail.val = val;
      return;
    }

    let currNode = this.head;
    for (let i = 0; i <= idx - 1; i++) {
      currNode = currNode.next;
    }
    currNode.val = val;
  }

  /** insertAt(idx, val): add node w/val before idx. */
  // create a new node with the val in the params; and set variable newNode to the new node
  //if idx ===0, just use unshift(val)
  //if idx===this.length, use push(val)
  //find node for (idx-1) as preNode, create variable nextNode for the node for the preNode.next
  //set the preNode.next to the newNode, and set the newNode.next to the nextNode
  insertAt(idx, val) {
    if (idx < 0 || idx > this.length) {
      throw 'invalid index';
    }
    if (idx === 0) {
      return this.unshift(val);
    }
    if (idx === this.length) {
      return this.push(val);
    }

    const newNode = new Node(val);

    let preNode = this.head;
    for (let i = 0; i <= idx - 2; i++) {
      preNode = preNode.next;
    }

    const nextNode = preNode.next;
    preNode.next = newNode;
    newNode.next = nextNode;
    this.length++;
  }

  /** removeAt(idx): return & remove item at idx, */
  //
  removeAt(idx) {}

  /** average(): return an average of all values in the list */

  average() {}
}

module.exports = LinkedList;
