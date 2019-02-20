function maxDepth(rootNode = null) {
  if (rootNode === null) return 0;
  //only root tree
  if (!(rootNode.left && rootNode.right)) return 1;

  // only left node

  if (rootNode.left && !rootNode.right) return maxDepth(rootNode.left) + 1;

  //only right  node
  if (!rootNode.left && rootNode.right) return maxDepth(rootNode.right) + 1;

  // both left and right

  if (rootNode.left && rootNode.right)
    return Math.max(maxDepth(rootNode.left), maxDepth(rootNode.right)) + 1;
}

module.exports = maxDepth;
