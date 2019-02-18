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
      console.log(this.tail.val);
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

  shift() {}

  /** getAt(idx): get val at idx. */

  getAt(idx) {}

  /** setAt(idx, val): set val at idx to val */

  setAt(idx, val) {}

  /** insertAt(idx, val): add node w/val before idx. */

  insertAt(idx, val) {}

  /** removeAt(idx): return & remove item at idx, */

  removeAt(idx) {}

  /** average(): return an average of all values in the list */

  average() {}
}

module.exports = LinkedList;
