function minDepth(rootNode = null) {
  //empty tree
  if (rootNode === null) return 0;
  //only root tree
  if (!(rootNode.left && rootNode.right)) return 1;

  // only left node

  if (rootNode.left && !rootNode.right) return minDepth(rootNode.left) + 1;

  //only right  node
  if (!rootNode.left && rootNode.right) return minDepth(rootNode.right) + 1;

  // both left and right

  if (rootNode.left && rootNode.right)
    return Math.min(minDepth(rootNode.left), minDepth(rootNode.right)) + 1;
}

module.exports = minDepth;
