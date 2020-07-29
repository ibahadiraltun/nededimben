import axios from 'axios'

const api = 'http://localhost:8081/api/search'

async function getPredictions(message) {
  const reqUrl = `${api}?url=${message}`
  try {
    const res = await axios.get(reqUrl)
    return res.data
  } catch (err) {
    console.error(err)
  }
}

export { getPredictions }