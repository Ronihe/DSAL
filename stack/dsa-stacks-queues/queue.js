/** Node: node for a queue. */

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

/** Queue: chained-together nodes where you can
 *  remove from the front or add to the back. */

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  /** enqueue(val): add new value to end of the queue. Returns undefined. */
  // create new node with val, set a variable newNode to the new node
  // if the queue is empty, set the first and last to the newNode
  // if the queue is not empty, set this.last.next to the newNode, and set the newNode as this.last
  enqueue(val) {
    const newNode = new Node(val);

    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
      this.size++;
      return;
    }
    this.last.next = newNode;
    this.last = newNode;
    this.size++;
  }

  /** dequeue(): remove the node from the start of the queue
   * and return its value. Should throw an error if the queue is empty. */
  //if there is only one in the queque, set the first and last to null
  dequeue() {
    if (!this.first) {
      throw new Error('cannnot dequeue since the queque is empty');
    }
    let removedVal = this.first.val;
    let newFirst = this.first.next;
    this.first = newFirst;
    this.size--;
    if (this.size === 0) {
      this.last = null;
    }
    return removedVal;
  }

  /** peek(): return the value of the first node in the queue. */

  peek() {
    return this.first.val;
  }

  /** isEmpty(): return true if the queue is empty, otherwise false */

  isEmpty() {
    if (this.size === 0) {
      return true;
    }
    return false;
  }
}

module.exports = Queue;
