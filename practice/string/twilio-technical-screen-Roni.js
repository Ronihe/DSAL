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

  while (endIdx <= message.length - 1) {
    let spaceIdx = startIdx + message.slice(startIdx, endIdx).lastIndexOf(' ');
    let subMessage;
    if (endIdx === spaceIdx + 1) {
      subMessage = message.slice(startIdx, spaceIdx);
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
