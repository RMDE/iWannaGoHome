import axios from '@api/http'

const UserApi = {
  login: function (user) {
    return axios.post('/token', user)
  }
}

export default UserApi
