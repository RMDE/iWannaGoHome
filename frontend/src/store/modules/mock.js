import MockApi from '@api/mock'

const state = {
  mocks: [],
  mocksStatus: 0// 监视获取状态，用于登录时监视
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
        commit('setMocksStatus', 1)
        commit('setMocks', res.data)
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
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
