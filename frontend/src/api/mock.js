import axios from './http'

const MockApi = {
  getMockList: function () {
    return axios.get('/mock/all')
  },
  fetchMock: function (mockId) {
    return axios.get('/mock/' + mockId)
  }
}

export default MockApi
