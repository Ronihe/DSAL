/** Node: node for a stack. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** Stack: chained-together nodes where you can
 *  remove from the top or add to the top. */

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  /** push(val): add new value to end of the stack. Returns undefined. */

  // if the stack is empty, the the first and last to the newNode
  //add tge value to the fist
  // if there is only one value after adding, set the last to the newNode too
  push(val) {
    const newNode = new Node(val);
    newNode.next = this.first;
    this.first = newNode;
    this.size++;

    if (this.size === 1) {
      this.last = newNode;
    }
  }

  /** pop(): remove the node from the top of the stack
   * and return its value. Should throw an error if the stack is empty. */

  pop() {}

  /** peek(): return the value of the first node in the stack. */

  peek() {}

  /** isEmpty(): return true if the stack is empty, otherwise false */

  isEmpty() {}
}

module.exports = Stack;
