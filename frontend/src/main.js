import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import heyUI from 'heyui'

// 使用HeyUI
Vue.use(heyUI)

// 引入样式，@less, defined in vue.config.js, is an alias to /src/assets/style
require('@style/app.less')

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
