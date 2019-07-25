import axios from './http'

const ProjectApi = {
  getProjectList: function () {
    return axios.get('/project/all')
  },
  fetchProject: function (projectId) {
    return axios.get('/project/' + projectId)
  },
  updateProject: function (projectId, project) {
    return axios.put('/project/' + projectId, project)
  },
  createProject: function (project) {
    return axios.post('/project', project)
  }
}

export default ProjectApi
