import axios from './http'

const MockApi = {
  getMockList: function () {
    return axios.get('/mock/all')
  },
  fetchMock: function (mockId) {
    return axios.get('/mock/' + mockId)
  },
  updateMock: function (mockId, mock) {
    return axios.put('/mock/' + mockId, mock)
  },
  createMock: function (mock) {
    return axios.post('/mock', mock)
  },
  abandonMock: function (mockId) {
    return axios.patch('/mock/' + mockId)
  }
}

export default MockApi
