import { PythonShell } from 'python-shell'

function runPredictHandler(args, callback) {
  PythonShell.run(
    './server/predict-handler.py',
    { args: args },
    (errors, output) => {
      output = JSON.parse(output[0])
      const res = {
        off: {
          neg: output[0][1][0],
          pos: output[0][1][1],
        },
        cw: {
          neg: output[1][1][0],
          pos: output[1][1][1]
        },
        sa: {
          neg: output[2][1][0],
          notr: output[2][1][1],
          pos: output[2][1][2]
        }
      }
      callback(JSON.stringify(res))
    }
  )
}

function getTweetData(url, callback) {
  PythonShell.run(
    './server/service/scripts/tweet-scraper.py', 
    { args: url },
    (err, results) => {
      if (!results) callback('error')
      runPredictHandler(results, callback)
    }
  )
}

function isTwitterLink(url) {
  return url.includes('twitter.com')
}

function getPredictions(url, callback) {
  if (isTwitterLink(url)) {
    // get tweet content
    getTweetData(url, callback)
  } else {
    // this is a text
    runPredictHandler(url, callback)
  }
}

export { getPredictions }
