const str =
  'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis ipsum vero debitis quam libero laudantium cumque accusantium quod, adipisci nemo atque dicta minus at temporibus inventore asperiores pariatur impedit est? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Expedita dolores ea dicta quo, laborum amet corporis facere unde architecto necessitatibus. Provident, voluptas? Culpa quasi, enim consequuntur vitae distinctio dolor soluta! Lorem ipsum dolor sit amet consectetur, adipisicing elit. Obcaecati dicta natus dignissimos laboriosam recusandae tem\\pore nisi nesciunt deserunt enim, alias, facilis, aspernatur culpa possimus. Itaque, illum totam. Doloremque, est aliquam! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa tempore velit magni repellat molestias fugiat, iusto veritatis esse quia adipisci sapiente modi aperiam dignissimos perferendis dolore voluptatem deserunt suscipit totam. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolor, ipsa recusandae quo saepe, libero rem odio consequuntur delectus quibusdam, molestiae quod itaque? Eum labore nostrum, numquam dignissimos beatae reprehenderit laborum!';

//it wont be longer than 9 messages
// part1 divide it by 160 length messages ending (1/8) which is included in the message
const messageCharLimit = 160;
const counterLen = 5; //e.g. (3/5)
const msgLen = messageCharLimit - counterLen;

function splitMessage(message) {
  // accepts a string and returns a array of sub-messages with max length of 160
  const messages = [];
  const msgNum = Math.ceil(message.length / msgLen); // this is the totoal length of the new array
  let startIdx = 0;
  let endIdx = startIdx + msgLen;

  for (let i = 1; i <= msgNum; i++) {
    let subMsg = str.slice(startIdx, endIdx) + `(${i}/${msgNum})`;
    messages.push(subMsg);
    startIdx += msgLen;
    endIdx = startIdx + msgLen;
  }

  return messages;
}

function splitMessagev2(message) {
  // same as the above but move the word to the next sub msg if the ending is the middle of the word
  const messages = [];
  let startIdx = 0;
  let endIdx = startIdx + msgLen;

  while (endIdx <= message.length - 1) {
    let spaceIdx = startIdx + str.slice(startIdx, endIdx).lastIndexOf(' ');
    let subMsg = str.slice(startIdx, spaceIdx);
    messages.push(subMsg);
    startIdx = spaceIdx + 1;
    endIdx = startIdx + msgLen;
  }

  if (startIdx < message.length - 1) {
    messages.push(message.slice(startIdx));
  }

  let result = messages.map((el, i) => {
    return el + `(${i + 1}/${messages.length})`;
  });

  return result;
}

//console.log(arrOfStr(str));
console.log(splitMessage(str));
//console.log(arrOfmoveSpace(str));


'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'split' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING message as parameter.
 */

function split(message) {
    const messageCharLimit = 160;
    const segmentLen = 5;
    const msgLen = messageCharLimit - segmentLen;
    const messages = [];
    //const msgNum = Math.ceil(message.length / msgLen);
    let startIdx = 0;
    let endIdx = startIdx + msgLen;
    if (message.length <= msgLen) {
        return [message];
    }

    
    // first iteration
    // for (let i = 0; i < msgNum; i++){
    //     let msg = message.slice(startIdx, endIdx);
    //     messages.push(msg+`(${i+1}/${msgNum})`);
    //     startIdx += msgLen;
    //     endIdx += msgLen;
    // }
    while (endIdx <= message.length - 1) {
        let spaceIdx = startIdx + message.slice(startIdx, endIdx + 1).lastIndexOf(' ');
        let subMessage;
        if (endIdx === spaceIdx) {
            subMessage = message.slice(startIdx, spaceIdx-1);
            spaceIdx-=1;
        } else {
            spaceIdx++;
            subMessage = message.slice(startIdx, spaceIdx);
        }
        messages.push(subMessage);
        startIdx = spaceIdx;
        endIdx = startIdx + msgLen;
    }

    if (startIdx < message.length - 1) {
        messages.push(message.slice(startIdx));
    }

    let finalMessages = messages.map((subMsg, i) => {
        return subMsg + `(${i + 1}/${messages.length})`;
    });

    return finalMessages;
}

function main() {