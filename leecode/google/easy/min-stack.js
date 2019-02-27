//https://leetcode.com/problems/min-stack/
class Node {
  constructor(val) {
    this.value = val;
    this.next = null;
    this.min = val;
    // this.min = Math.min(this.value, this.next.min);
  }
}
/**
 * initialize your data structure here.
 */
class MinStack {
  constructor() {
    this.top = null;
    this.tail = null;
  }

  /**
   * @param {number} x
   * @return {void}
   */
  push(val) {
    const newNode = new Node(val);
    if (!this.top) {
      this.top = newNode;
      this.tail = newNode;
    } else if (!this.top.next) {
      this.top.next = newNode;
      this.tail = newNode;
      this.tail.min = Math.min(this.top.min, newNode.min);
    } else {
      this.tail.next = newNode;
      console.log(this.tail.min, newNode.min);
      newNode.min = Math.min(this.tail.min, newNode.min);
      this.tail = newNode;
    }
    // console.log(newNode);
  }
  /**
   * @return {void}
   */
  pop() {
    //if there no node in the stack return false
    if (!this.top) return false;
    //if there is only one node in the stack, make top and tail as null
    if (!this.top.next) {
      this.top = null;
      this.tail = null;
      return;
    }
    //else
    let currNode = this.top;
    while (currNode.next.next) {
      currNode = currNode.next;
    }
    this.tail = currNode;
  }
  /**
   * @return {number}
   */
  top() {
    return this.top.value;
  }
  /**
   * @return {number}
   */
  getMin() {
    if (!this.top) return false;
    return this.tail.min;
  }

  print() {
    const arr = [];

    let currNode = this.top;
    if (!currNode) return arr;
    while (currNode.next) {
      arr.push(currNode.value);
    }
    arr.push(currNode.value);
    return arr;
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = Object.create(MinStack).createNew()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
let newMinStack = new MinStack();
//console.log(newMinStack.print());
newMinStack.push(-2);
//console.log(newMinStack.print());
newMinStack.push(-5);
newMinStack.push(-5);
newMinStack.push(-5);
newMinStack.push(-10);
console.log(newMinStack.getMin());
