const reverseLettersInPlace = require('./reverseLettersInPlace');

describe('merged correctly', () => {
  const test = [1, 2, 3, 4];
  it('merged correctly', () => {
    expect(reverseLettersInPlace(test)).toEqual([4, 3, 2, 1]);
  });
});
