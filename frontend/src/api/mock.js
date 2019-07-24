import axios from './http'

const MockApi = {
  getMockList: function () {
    return axios.get('/mock/all')
  }
}

export default MockApi
