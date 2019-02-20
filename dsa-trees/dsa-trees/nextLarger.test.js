const nextLarger = require("./nextLarger");

describe("nextLarger", () => {
  it("handles simple trees", () => {
    let node1 = { left: null, right: null, value: 5 };
    let node2 = { left: null, right: null, value: 5 };
    let rootNode = { left: node1, right: node2, value: 6 };
    
    expect(nextLarger(rootNode, 5)).toBe(6);
    expect(nextLarger(rootNode, 6)).toBe(null);
  })
  it("handles empty trees", () => {
    expect(nextLarger()).toBe(null);
  })
  it("handles more complex trees", () => {
    let node6 = { left: null, right: null, value: 1 }
    let node5 = { left: null, right: null, value: 1 }
    let node4 = { left: null, right: null, value: 2 }
    let node3 = { left: node4, right: node6, value: 3 }
    let node2 = { left: node3, right: node5, value: 4 }
    let node1 = { left: null, right: null, value: 5 }
    let rootNode = { left: node1, right: node2, value: 6 }
    
    expect(nextLarger(rootNode,1)).toBe(2);
    expect(nextLarger(rootNode,2)).toBe(3);
    expect(nextLarger(rootNode,3)).toBe(4);
    expect(nextLarger(rootNode,4)).toBe(5);
    expect(nextLarger(rootNode,5)).toBe(6);
    expect(nextLarger(rootNode,6)).toBe(null);
  });
});