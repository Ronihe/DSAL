/**
 * @param {string[]} emails
 * @return {number}
 * https://leetcode.com/problems/unique-email-addresses/
 */
function numUniqueEmails(emails) {
  const emailSet = new Set();

  for (let email of emails) {
    let formattedEmail = _reformat(email);
    emailSet.add(formattedEmail);
  }
  //split by @ for local part, split by '+', get the first part, split the firt part by '.'
  function _reformat(email) {
    let local = email.split('@')[0];
    let domain = email.split('@')[1];

    let formattedLocal = local
      .split('+')[0]
      .split('.')
      .join('');
    return formattedLocal + '@' + domain;
  }
  return emailSet.size;
}

let emails = [
  'test.email+alex@leetcode.com',
  'test.e.mail+bob.cathy@leetcode.com',
  'testemail+david@lee.tcode.com'
];
console.log(numUniqueEmails(emails));
