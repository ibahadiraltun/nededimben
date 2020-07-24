const express = require('express')
const app = express()

import { getTweetData } from './service/tweet-handler'

const port = process.env.PORT || 8081;

// localhost:3000 text
app.get('/', (req, res) => {
  var responseMessage = 'This is NLPIFY web-app.' +
                  ' To test it, please pass your tweet url to /search.' +
                  ' Sample request:' +
                  ' http://localhost:3000/search?url={tweet_url}';
  res.send(responseMessage); 
});

app.get('/search', (req, res) => {
  const url = req.query.url
  if (url == '' || url == null) {
    res.send('Please enter a valid url');
  } else {
    getTweetData(url, (data) => {
      res.send(data)
    })
  }
});

const server = app.listen(port, () => console.log(`Listening on port: ${port}...`));
