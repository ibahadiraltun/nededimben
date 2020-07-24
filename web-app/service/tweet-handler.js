const spawn = require("child_process").spawn;

async function getTweetData(url, callback) {
  const pythonProcess = spawn('python', ["service/scrapers/tweet-scraper.py", url]);
  pythonProcess.stdout.on('data', (data) => {
    callback(data.toString())
  });
}

export { getTweetData }
