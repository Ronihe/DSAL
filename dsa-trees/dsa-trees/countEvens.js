class Node {
  constructor(val, children = []) {
    this.val = val;
    this.children = children;
  }
}
class Tree {
  constructor() {
    this.root = null;
  }

  sumValues() {
    if (this.root === null) return 0;

    let total = 0;
    let toVisitStack = [this.root];

    while (toVisitStack.length) {
      let currNode = toVisitStack.pop();

      total += currNode.val;
      for (let child of currNode.children) toVisitStack.push(child);
    }
    return total;
  }

  countEvens() {
    if (this.root === null) return 0;
    let totalEven = 0;
    let toVisitStack = [this.root];
    while (toVisitStack.length) {
      let currNode = toVisitStack.pop();
      if (currNode.val % 2 === 0) totalEven++;
      for (let child of currNode.children) toVisitStack.push(child);
    }
    return totalEven;
  }
}

module.exports = { Tree, Node };
