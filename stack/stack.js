/**
 * LinkedList to implement stacl
 */
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
  //pushing a value on the top of a stack
  // create a node with the value
  //if there is no nodes in the stack set the first and last property as the newly created node.
  //if there is one alread, set the first to the new created

  push(value) {
    let newNode = new Node(value);
    if (this.size === 0) {
      this.first = newNode;
      this.last = newNode;
    }
    let temp = this.first;
    this.first = newNode;
    this.first.next = temp;
    return ++this.size;
  }

  //pop remove the value from the top of the stack
  // if there is no nodes in the statk retuen null;
  // create a variable caleed popedValue for this.first
  //if there is only value, make first and last as null, return popedValue
  // else remove the first one and make the first.next as new first.
  pop() {
    if (this.size === 0) {
      return null;
    }

    let poppedVal = this.first;
    if (this.size === 1) {
      this.first = null;
      this.last = null;
      this.size = 0;
    } else {
      this.first.poppedVal.next;
      this.size--;
    }
    return poppedVal;
  }
}

let newStack = new Stack();
newStack.push(1);
console.log(newStack.push(2));
