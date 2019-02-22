const bubbleSort = require("./bubble")

describe('bubbleSort', function () {
  it('should exist', function () {
    expect(typeof bubbleSort).toBe('function', "did you remember to define the 'bubbleSort' function?");
  });

  it('should sort numbers in ascending order if no comparator is provided', function () {
    expect(bubbleSort([4, 20, 12, 10, 7, 9])).toEqual(
      [4, 7, 9, 10, 12, 20],
      "bubbleSort([4, 20, 12, 10, 7, 9]) should equal [4, 7, 8, 10, 12, 20]"
    );
    expect(bubbleSort([0, -10, 7, 4])).toEqual(
      [-10, 0, 4, 7],
      "bubbleSort([0, -10, 7, 4]) should equal [-10, 0, 4, 7]"
    );
    expect(bubbleSort([1, 2, 3])).toEqual(
      [1, 2, 3],
      "bubbleSort([1, 2, 3]) should equal [1, 2, 3]"
    );
    expect(bubbleSort([])).toEqual(
      [],
      "bubbleSort([]) should be []"
    );
    var nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
    expect(bubbleSort(nums)).toEqual(
      [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342],
      "bubbleSort([4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]) should equal [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]"
    );
  });

  it('should sort by the comparator if a comparator is provided', function () {
    var kitties = ["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"];

    function strComp(a, b) {
      if (a < b) { return -1; }
      else if (a > b) { return 1; }
      return 0;
    }

    var moarKittyData = [{
      name: "LilBub",
      age: 7
    }, {
      name: "Garfield",
      age: 40
    }, {
      name: "Heathcliff",
      age: 45
    }, {
      name: "Blue",
      age: 1
    }, {
      name: "Grumpy",
      age: 6
    }];

    function oldestToYoungest(a, b) {
      return b.age - a.age;
    }

    expect(bubbleSort(kitties, strComp)).toEqual(
      ["Blue", "Garfield", "Grumpy", "Heathcliff", "LilBub"],
      'bubbleSort(["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"], strComp) should equal ["Blue", "Garfield", "Grumpy", "Heathcliff", "LilBub"]'
    );
    expect(bubbleSort(moarKittyData, oldestToYoungest)).toEqual([{
      name: "LilBub",
      age: 7
    }, {
      name: "Garfield",
      age: 40
    }, {
      name: "Heathcliff",
      age: 45
    }, {
      name: "Blue",
      age: 1
    }, {
      name: "Grumpy",
      age: 6
    }].sort(oldestToYoungest),
      "bubbleSort(moarKittyData, oldestToYoungest) should sort the kitties from oldest to youngest.")
  });
});
