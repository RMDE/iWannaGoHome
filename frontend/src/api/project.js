import axios from './http'

const ProjectApi = {
  getProjectList: function () {
    return axios.get('/project/all')
  }
}

export default ProjectApi
