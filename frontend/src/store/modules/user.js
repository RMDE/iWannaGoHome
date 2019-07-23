import UserApi from '@api/user'
import { setCookie, delCookie, getCookie } from '../../utils/cookie'

const state = {
  email: null,
  token: null,
  status: 0// 登录状态，用于登录时监视
}

const mutations = {
  setToken (state, val) {
    state.token = val
  },
  setMail (state, val) {
    state.email = val
  },
  setStatus (state, val) {
    state.status = val
  }
}

const getters = {
  status: state => state.status,
  email: state => state.email,
  token: () => {
    return getCookie('token')
  }
}

const actions = {
  login ({ commit, state }, user) {
    // 状态重置
    UserApi.login(user).then((res) => {
      if (res.status === 200) {
        commit('setToken', res.data.token)
        commit('setMail', res.data.email)
        commit('setStatus', 1)
        setCookie('token', state.token)
      }
    }).catch((e) => {
      commit('setStatus', -1)
      console.log(e)
    })
  },
  logout ({ commit }) {
    commit('setUid', null)
    commit('setToken', null)
    commit('setStatus', null)
    delCookie('token')
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
