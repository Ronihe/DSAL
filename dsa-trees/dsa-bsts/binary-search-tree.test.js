const BinarySearchTree = require('./binary-search-tree');

describe('insert', function() {
  it('inserts_a_node_at_the_correct_position', function() {
    var binarySearchTree = new BinarySearchTree();
    binarySearchTree.insert(15);
    binarySearchTree.insert(20);
    binarySearchTree.insert(10);
    binarySearchTree.insert(12);
    expect(binarySearchTree.root.value).toEqual(15);
    expect(binarySearchTree.root.right.value).toEqual(20);
    expect(binarySearchTree.root.left.right.value).toEqual(12);
  });
  it('inserts_a_node_at_the_root_if_there_is_nothing_there', function() {
    var binarySearchTree = new BinarySearchTree();
    binarySearchTree.insert(15);
    expect(binarySearchTree.root.value).toEqual(15);
    expect(binarySearchTree.root.left).toBe(null);
    expect(binarySearchTree.root.right).toBe(null);
  });
});

describe('find', function() {
  it('find_finds_a_node_correctly', function() {
    let binarySearchTree = new BinarySearchTree();
    binarySearchTree
      .insert(15)
      .insert(20)
      .insert(10)
      .insert(12);
    var foundNode = binarySearchTree.find(20);
    expect(foundNode.value).toBe(20);
    expect(foundNode.left).toBe(null);
    expect(foundNode.right).toBe(null);
  });
  it('find_returns_undefined_if_a_node_is_not_found', function() {
    let binarySearchTree = new BinarySearchTree();

    binarySearchTree
      .insert(15)
      .insert(20)
      .insert(10)
      .insert(12);
    var foundNode = binarySearchTree.find(120);
    expect(foundNode).toBe(undefined);
  });
});

// describe('DFS', function () {
//   it('returns_an_array_of_values_found_with_DFS_In_Order', function () {
//     let binarySearchTree = new BinarySearchTree
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
//     expect(binarySearchTree.DFSInOrder()).toEqual([1, 5, 10, 12, 15, 20, 50])
//   });
//   it('returns_an_array_of_values_found_with_DFS_Pre_Order', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
//     expect(binarySearchTree.DFSPreOrder()).toEqual([15, 10, 1, 5, 12, 20, 50])
//   });
//   it('returns_an_array_of_values_found_with_DFS_Post_Order', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
//     expect(binarySearchTree.DFSPostOrder()).toEqual([5, 1, 12, 10, 50, 20, 15])
//   });
// });

// describe('BFS', function () {
//   it('should return the correct output', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
//     expect(binarySearchTree.breadthFirstSearch()).toEqual([15, 10, 20, 1, 12, 50, 5])
//   });
// });

// describe('remove', function () {
//   it('remove_should_correctly_remove_a_node_with_no_children', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
//     binarySearchTree.remove(50)
//     expect(binarySearchTree.root.right.value).toBe(20)
//     expect(binarySearchTree.root.right.right).toBe(null)

//     binarySearchTree.remove(5)
//     expect(binarySearchTree.root.left.left.value).toBe(1)
//     expect(binarySearchTree.root.left.left.right).toBe(null)
//   });
//   it('remove_should_correctly_remove_a_node_with_one_child', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)

//     binarySearchTree.remove(1)
//     expect(binarySearchTree.root.left.left.value).toBe(5)
//     expect(binarySearchTree.root.left.left.left).toBe(null)
//     expect(binarySearchTree.root.left.left.right).toBe(null)

//     binarySearchTree.remove(20)
//     expect(binarySearchTree.root.right.value).toBe(50)
//     expect(binarySearchTree.root.right.right).toBe(null)
//     expect(binarySearchTree.root.right.left).toBe(null)
//   });
//   it('remove_should_correctly_remove_a_node_with_two_children', function () {
//     let binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50).insert(60).insert(30).insert(25).insert(23).insert(24).insert(70)

//     binarySearchTree.remove(10)
//     expect(binarySearchTree.root.left.value).toBe(12)
//     expect(binarySearchTree.root.left.left.value).toBe(1)
//     expect(binarySearchTree.root.left.left.right.value).toBe(5)

//     binarySearchTree.remove(50)
//     expect(binarySearchTree.root.right.value).toBe(20)
//     expect(binarySearchTree.root.right.right.value).toBe(60)
//     expect(binarySearchTree.root.right.right.left.value).toBe(30)
//   });
//   it('should_remove_a_node_with_two_children_and_handle_the_children_of_the_removed_node', function () {
//     var binarySearchTree = new BinarySearchTree();
//     binarySearchTree
//       .insert(22)
//       .insert(49)
//       .insert(85)
//       .insert(66)
//       .insert(95)
//       .insert(90)
//       .insert(100)
//       .insert(88)
//       .insert(93)
//       .insert(89)

//     binarySearchTree.remove(85);
//     expect(binarySearchTree.root.right.right.value).toBe(88) // 88
//     expect(binarySearchTree.root.right.right.right.left.left.value).toBe(89) // 89
//   });
// });

// describe('findSecondLargest', function () {
//   it('finds the 2nd largest', function () {
//     var binarySearchTree = new BinarySearchTree()
//     binarySearchTree.insert(15)
//     binarySearchTree.insert(20)
//     binarySearchTree.insert(10)
//     binarySearchTree.insert(12)
//     expect(binarySearchTree.findSecondLargest()).toEqual(15)

//     var binarySearchTree2 = new BinarySearchTree()
//     expect(binarySearchTree2.findSecondLargest()).toEqual(undefined)

//   });
// });

// describe("isBalanced", function() {
//   it("checks if it is balanced", function() {
//     var binarySearchTree = new BinarySearchTree();
//     binarySearchTree.insert(15);
//     binarySearchTree.insert(20);
//     binarySearchTree.insert(10);
//     binarySearchTree.insert(12);
//     expect(binarySearchTree.isBalanced()).toEqual(true);

//     var binarySearchTree2 = new BinarySearchTree();
//     binarySearchTree2.insert(5);
//     expect(binarySearchTree2.isBalanced()).toEqual(true);
//     binarySearchTree2.insert(6);
//     expect(binarySearchTree2.isBalanced()).toEqual(true);
//     binarySearchTree2.insert(7);
//     expect(binarySearchTree2.isBalanced()).toEqual(false);
//   });
// });
