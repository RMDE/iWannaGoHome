import ProjectApi from '@api/project'
import Vue from 'vue'

const state = {
  projects: [],
  status: 0// 监视获取状态
}

const mutations = {
  setProjects (state, val) {
    state.projects = val
  },
  setStatus (state, val) {
    state.status = val
  }
}

const getters = {
  status: state => state.status,
  projects: state => state.projects
}

const actions = {
  getProjectList ({ commit }) {
    // 状态重置
    commit('setStatus', 0)
    ProjectApi.getProjectList().then((res) => {
      if (res.status === 200) {
        commit('setProjects', res.data)
        commit('setStatus', 1)
      }
    }).catch((e) => {
      if (e.response.status === 404) {
        // 数据库中不存在，所以会返回404
        commit('setProjects', [])
        commit('setStatus', 1)
      } else {
        commit('setStatus', -1)
      }
      console.log(e)
    })
  },
  createProject ({ commit }, obj) {
    let result
    ProjectApi.createProject(obj).then(() => {
      Vue.prototype.$Notice['success']('创建成功')
      result = true
    }).catch((e) => {
      console.log(e)
      Vue.prototype.$Notice['error']('创建失败')
      result = false
    })
    return result
  },
  updateProject ({ commit }, obj) {
    let result
    ProjectApi.updateProject(obj.id, obj.project).then(() => {
      Vue.prototype.$Notice['success']('更新成功')
      result = true
    }).catch((e) => {
      console.log(e)
      Vue.prototype.$Notice['error']('更新失败')
      result = false
    })
    return result
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
