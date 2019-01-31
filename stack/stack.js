/**
 * LinkedList to implement stacl
 */

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

//pushing a value on the top of a stack
// create a node with the value
//if there is no nodes in the stack set the first and last property as the newly created node.
//if there is one alread, set the first to the new created
