const minDepth = require("./minDepth");

describe("minDepth", () => {
  it("handles simple trees", () =>{
    let node1 = { left: null, right: null, value: 5 };
    let node2 = { left: null, right: null, value: 5 };
    let rootNode = { left: node1, right: node2, value: 6 };
    expect(minDepth(rootNode)).toBe(2);
  })
  it("handles empty trees", () => {
    expect(minDepth()).toBe(0);
  })
  it("handles more complex trees", () => {
    let node6 = { left: null, right: null, value: 1 }
    let node5 = { left: null, right: null, value: 1 }
    let node4 = { left: null, right: null, value: 2 }
    let node3 = { left: node4, right: node6, value: 3 }
    let node2 = { left: node3, right: node5, value: 4 }
    let node1 = { left: null, right: null, value: 5 }
    let rootNode = { left: node1, right: node2, value: 6 }
    
    expect(minDepth(rootNode)).toBe(2);
  });
});