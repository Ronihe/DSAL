## Traversal:
- visit the node in the data structure
1. 层序遍历（Level order）
2. 先序遍历（Pre order）
3. 中序遍历（In order）
4. 后序遍历（Post order）

我们在之前的课程中，已经学习过了二叉树的层序遍历，也就是使用 BFS 算法来获得二叉树的分层信息。通过 BFS 获得的顺序我们也可以称之为 BFS Order。而剩下的三种遍历，都需要通过深度优先搜索的方式来获得。而这一小节中，我们将讲一下通过深度优先搜索（DFS）来获得的节点顺序，

先序遍历 / 中序遍历 / 后序遍历

### 先序遍历（又叫先根遍历、前序遍历）
首先访问根结点，然后遍历左子树，最后遍历右子树。遍历左、右子树时，仍按先序遍历。若二叉树为空则返回。

该过程可简记为根左右，注意该过程是递归的。如图先序遍历结果是：ABDECF。
```
# 将根作为root，空list作为result传入，即可得到整棵树的遍历结果
def traverse(root, result):
    if not root:
        return
    result.append(root.val)
    traverse(root.left, result)
    traverse(root.right, result)
```