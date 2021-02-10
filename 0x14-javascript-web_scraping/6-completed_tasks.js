#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request(urlPath, function (err, res, body) {
  if (err) { console.err(err); }
  const allMembers = JSON.parse(body);
  const tasksChecked = {};

  allMembers.forEach(completed => {
    if (completed.completed === true) {
      const UserDone = completed.userId;

      if (UserDone in tasksChecked) {
        tasksChecked[UserDone]++;
      } else {
        tasksChecked[UserDone] = 1;
      }
    }
  });
  console.log(tasksChecked);
});
