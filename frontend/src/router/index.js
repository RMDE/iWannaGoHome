import Vue from 'vue'
import Router from 'vue-router'
import routes from './routes'
import heyUI from 'heyui'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: routes
})

// 显示页面加载进度条
router.afterEach(() => {
  heyUI.$LoadingBar.success()
})

export default router
