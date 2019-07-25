import Vue from 'vue'
import Vuex from 'vuex'

import user from './modules/user'
import mock from './modules/mock'
import project from './modules/project'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user,
    mock,
    project
  }
})
