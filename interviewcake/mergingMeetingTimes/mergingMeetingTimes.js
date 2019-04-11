//brute force BigO Time: O(N^2) Space: O(1)
function mergingMeetingTimes_V1(array) {
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

//better solution BigO Time: O(nlog(n)) Space: O(1)
//sort the input the array of meetings by the startTime
// loop throught the sorted the array
function mergingMeetingTimes_V2(array) {
  array.sort((a, b) => {
    a.startTime - b.startTime;
  });

  for (let i = 1; i < array.length; i++) {
    let preTime = array[i - 1];
    let currTime = array[i];

    if (
      preTime.startTime < currTime.startTime &&
      currTime.startTime < preTime.endTime
    ) {
      array[i - 1].endTime = Math.max(array[i - 1].endTime, array[i].endTime);
      array.splice(i, 1);
    }
  }

  return array;
}

module.exports = mergingMeetingTimes_V2;
