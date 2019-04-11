//brute force

function mergingMeetingTimes(array) {
  let indicator = true;
  while (indicator) {
    indicator = false;
    for (let i = 1; i < array.length; i++) {
      let preTime = array[i - 1];
      let currTime = array[i];

      if (
        preTime.startTime < currTime.startTime &&
        currTime.startTime < preTime.endTime
      ) {
        array[i - 1].endTime = Math.max(array[i - 1].endTime, array[i].endTime);
        array.splice(i, 1);
        indicator = true;
      } else if (
        currTime.startTime < preTime.startTime &&
        preTime.startTime < currTime.endTime
      ) {
        array[i].endTime = Math.max(array[i - 1].endTime, array[i].endTime);
        array.splice(i - 1, 1);
        indicator = true;
      }
    }
  }
  return array;
}

module.exports = mergingMeetingTimes;
