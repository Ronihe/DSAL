class BinarySearchNode {
  constructor(val, left = null, right = null) {
    this.value = val;
    this.left = left;
    this.right = right;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  // create a new node
  //if the root is null, make the newnode as the root;
  //find the spot when the left spot is smaller than the
  insert(val) {
    const newBinNode = new BinarySearchNode(val);

    if (this.root === null) {
      this.root = newBinNode;
      console.log(this);

      return this;
    }

    let currNode = this.root;

    while (currNode) {
      if (currNode.value > val) {
        //if there is no left node, add the currNode to the left of the node
        if (!currNode.left) {
          currNode.left = newBinNode;
          console.log(this);
          return this;
        }
        //if there is already left node, check the left node
        currNode = currNode.left;
      }
      //check the right
      if (currNode.value < val) {
        if (!currNode.right) {
          currNode.right = newBinNode;
          console.log(this);

          return this;
        }
        currNode = currNode.right;
      }
    }
  }
}
module.exports = BinarySearchTree;
