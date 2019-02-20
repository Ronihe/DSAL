const {Node, areCousins} = require("./areCousins")

describe("areCousins", () => {
  it("returns true if they are cousins, false if not", ()=>{
    let n1 = new Node(1);
    let n2 = new Node(2);
    let n3 = new Node(3);
    let n4 = new Node(4);
    let n5 = new Node(5);
    let n6 = new Node(6);
    let n7 = new Node(7);

    n1.left = n2;
    n1.right = n3;
    n2.left = n4;
    n2.right = n5;
    n3.left = n6;
    n3.right = n7;

    expect(areCousins(n1, n4, n6)).toBe(true) 
    expect(areCousins(n1, n4, n7)).toBe(true) 
    expect(areCousins(n1, n5, n6)).toBe(true) 
    expect(areCousins(n1, n5, n7)).toBe(true) 
    expect(areCousins(n1, n2, n3)).toBe(false) 
    expect(areCousins(n1, n4, n5)).toBe(false) 
    expect(areCousins(n1, n6, n7)).toBe(false) 
    expect(areCousins(n1, n4, n3)).toBe(false) 
    expect(areCousins(n1, n1, n3)).toBe(false) 
  })
})

