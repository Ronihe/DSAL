const { Tree, Node } = require("./numGreater")

describe("numGreater", () => {
  it("counts nested values", () => {
    let n = new Node(1);
    let n2 = new Node(2);
    let n3 = new Node(3);
    let n4 = new Node(4);
    let n5 = new Node(5);
    let n6 = new Node(6);
    let n7 = new Node(7);
    let n8 = new Node(8);

    n.children = [n2, n3, n4];

    n4.children.push(n5, n6);
    n6.children.push(n7);
    n7.children.push(n8);

    let t = new Tree();
    t.root = n;
    expect(t.numGreater(4)).toEqual(4);
  });
  it("counts smaller values", () => {
    let n = new Node(1);
    let n2 = new Node(2);

    n.children.push(n2)

    let t = new Tree();
    t.root = n;
    expect(t.numGreater(3)).toEqual(0)
  })
  it("sums up an empty tree", () => {
    expect((new Tree).numGreater()).toEqual(0);
  });
})
