// implement queue with linkedList

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  //start a queue,
  //accept a value
  //if there is no node in the queue, set the first and last as the new node
  //else add the new node to the end
  enqueue(value) {
    let newNode = new Node(value);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    }
    this.last.next = newNode;
    this.last = newNode;
    this.size++;
    return this.size;
  }

  //remove from the beginning of the queue
  //if there no values in the queue, return null
  //set the this.last to a new variable
  // if there is only one value in the queue, set the this.first, this.last as null
  //if there are more than one value, remove the first and set the
  dequeue() {
    if (!this.first) {
      return null;
    }
    let deququedVal = this.first;
    if (this.size === 1) {
      this.last = null;
    }
    this.first = this.first.next;
    this.size--;
    return deququedVal.value;
  }
}

let newQ = new Queue();
console.log(newQ.enqueue(1));
console.log(newQ.enqueue(2));
console.log(newQ.dequeue());
