#!/usr/bin/node

const request = require('request');
if (process.argv.length === 3) {
  const myArgs = process.argv.slice(2);
  const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
  const options = { json: true };

  request(url, options, async function (error, res, body) {
    if (error) {
      console.log(error);
    } else {
      for (const char of body.characters) {
        const ret = () => {
          return new Promise((resolve, reject) => {
            request(char, options, function (error, res, body) {
              if (error) { console.log(error); } else {
                resolve(body.name);
              }
            });
          });
        };
        console.log(await ret());
      }
    }
  });
}
