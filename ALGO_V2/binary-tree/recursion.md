## 递归三要素

1. 递归的定义
每一个递归函数，都需要有明确的定义，有了正确的定义以后，才能够对递归进行拆解。

```
def maxDepth(root):
代表 以 root 开头的子树的最大深度是多少。

```
```buildoutcfg
def preorder(root, result):
代表 将 root 开头的子树的前序遍历放到 result 里面

```

2. 递归的拆解

一个大问题如何拆解为若干个小问题去解决。
```buildoutcfg
leftDepth = maxDepth(root.left)
rightDepth = maxDepth(root.right)
return max(leftDepth, rightDepth) + 1
```
整棵树的最大深度，可以拆解为先计算左右子树深度，然后在左右子树深度中找到最大值+1来解决。

```buildoutcfg
result.append(root)
preorder(root.left, result)
perorder(root.right, result)
```
一棵树的前序遍历可以拆解为3个部分：

根节点自己（root）
左子树的前序遍历
右子树的前序遍历
所以对应的，我们把这个递归问题也拆分为三个部分来解决：

先把 root 放到 result 里 --> result.add(root);
再把左子树的前序遍历放到 result 里 --> preorder(root.left, result)。回想一下递归的定义，是不是正是如此？
再把右子树的前序遍历放到 result 里 --> preorder(root.right, result)。

3. 递归的出口

什么时候可以直接知道答案，不用再拆解，直接 return
```buildoutcfg
# 二叉树的最大深度
if not root:
    return 0
一棵空的二叉树，可以认为是一个高度为0的二叉树。
```

# Binary search tree
## 定义
二叉搜索树（Binary Search Tree，又名排序二叉树，二叉查找树，通常简写为BST）定义如下：
空树或是具有下列性质的二叉树：
（1）若左子树不空，则左子树上所有节点值均小于或等于它的根节点值；
（2）若右子树不空，则右子树上所有节点值均大于根节点值；
（3）左、右子树也为二叉搜索树；

BST 的特性
按照中序遍历（inorder traversal）打印各节点，会得到由小到大的顺序。
在BST中搜索某值的平均情况下复杂度为O(logN)，最坏情况下复杂度为O(N)，其中N为节点个数。将待寻值与节点值比较，若不相等，则通过是小于还是大于，可断定该值只可能在左子树还是右子树，继续向该子树搜索。
在balanced BST中查找某值的时间复杂度为O(logN)。

BST 的作用
通过中序遍历，可快速得到升序节点列表。
在BST中查找元素，平均情况下时间复杂度是O(logN)O(logN)；插入新节点，保持BST特性平均情况下要耗时O（logN）。（参考链接）。
和有序数组的对比：有序数组查找某元素可以用二分法，时间复杂度是O（logN）；但是插入新元素，维护数组有序性要耗时O（N）。

## 什么是平衡二叉搜索树

定义
平衡二叉搜索树（Balanced Binary Search Tree，又称为AVL树，有别于AVL算法）是二叉树中的一种特殊的形态。二叉树当且仅当满足如下两个条件之一，是平衡二叉树：

空树。
左右子树高度差绝对值不超过1且左右子树都是平衡二叉树。

### AVL树的高度为 O(logN)

当AVL树有N个节点时，高度为O(logN)O(logN)。为何？
试想一棵满二叉树，每个节点左右子树高度相同，随着树高的增加，叶子容量指数暴增，故树高一定是O(logN)O(logN)。而相比于满二叉树，AVL树仅放宽一个条件，允许左右两子树高度差1，当树高足够大时，可以把1忽略。如图是高度为9的最小AVL树，若节点更少，树高绝不会超过8，也即为何AVL树高会被限制到O(logN)O(logN)，因为树不可能太稀疏。严格的数学证明复杂,略去。

### AVL树有什么用？
最大作用是保证查找的最坏时间复杂度为O(logN)。而且较浅的树对插入和删除等操作也更快。






