import MockApi from '@api/mock'
import Vue from 'vue'

const state = {
  mocks: [],
  mocksStatus: 0// 监视获取状态
}

const mutations = {
  setMocks (state, val) {
    state.mocks = val
  },
  setMocksStatus (state, val) {
    state.mocksStatus = val
  }
}

const getters = {
  mocksStatus: state => state.mocksStatus,
  mocks: state => state.mocks
}

const actions = {
  getMockList ({ commit }) {
    // 状态重置
    commit('setMocksStatus', 0)
    MockApi.getMockList().then((res) => {
      if (res.status === 200) {
        commit('setMocks', res.data)
        commit('setMocksStatus', 1)
      }
    }).catch((e) => {
      if (e.response.status === 404) {
        // 数据库中不存在，所以会返回404
        commit('setMocks', [])
        commit('setMocksStatus', 1)
      } else {
        commit('setMocksStatus', -1)
      }
      console.log(e)
    })
  },
  createMock ({ commit }, obj) {
    let result
    MockApi.createMock(obj).then(() => {
      Vue.prototype.$Notice['success']('创建成功')
      result = true
    }).catch((e) => {
      console.log(e)
      Vue.prototype.$Notice['error']('创建失败')
      result = false
    })
    return result
  },
  updateMock ({ commit }, obj) {
    let result
    MockApi.updateMock(obj.id, obj.mock).then(() => {
      Vue.prototype.$Notice['success']('更新成功')
      result = true
    }).catch((e) => {
      console.log(e)
      Vue.prototype.$Notice['error']('更新失败')
      result = false
    })
    return result
  },
  abandonMock ({ commit }, mockId) {
    let result
    MockApi.abandonMock(mockId).then(() => {
      Vue.prototype.$Notice['success']('操作成功')
      result = true
    }).catch((e) => {
      console.log(e)
      Vue.prototype.$Notice['error']('操作失败')
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
