import { getPredictions } from './service/req-handler'

const express = require('express')
const app = express()
const cors = require('cors')

const port = process.env.PORT || 8081

app.use(cors())

// localhost:8081
app.get('/', (req, res) => {
  var responseMessage = 'This is NLPIFY web-app.' +
                  ' To test it, please pass your tweet url to /search.' +
                  ' Sample request:' +
                  ' http://localhost:8081/search?url={tweet_url}'
  res.send(responseMessage)
});

app.get('/api/search', (req, res) => {
  const url = req.query.url
  if (url == '' || url == null) {
    res.send('Please enter a valid url')
  } else {
    getPredictions(url, (data) => {
      res.send(data)
    })
  }
})

const server = app.listen(port, () => console.log(`Server is listening on port: ${port}...`))
