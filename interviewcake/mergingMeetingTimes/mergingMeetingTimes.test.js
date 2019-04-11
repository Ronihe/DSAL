const mergingMeetingTimes = require('./mergingMeetingTimes');

describe('merged correctly', () => {
  const test = [{ startTime: 1, endTime: 5 }, { startTime: 2, endTime: 3 }];
  it('merged correctly', () => {
    expect(mergingMeetingTimes(test)).toEqual([{ startTime: 1, endTime: 5 }]);
  });
});


