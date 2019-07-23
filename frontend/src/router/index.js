import Vue from 'vue'
import Router from 'vue-router'
import routes from './routes'
import heyUI from 'heyui'
import { getCookie, setCookie } from '../utils/cookie'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: routes
})

// 显示页面加载进度条
router.beforeEach((to, from, next) => {
  heyUI.$LoadingBar.start()
  next()
  let token = getCookie('token')

  if (token) {
    setCookie('token', token)// 延长cookie有效期
  }

  if (to.name === 'login') {
    // 如果已经登录
    if (token) {
      router.push({ name: 'consoleSystem' })
    }
  }
  // 需要登录的路由
  if (to.meta.needLogin) {
    if (token) {
      next()
    } else {
      router.push({ name: 'login' })
    }
  } else {
    next()
  }
})

router.afterEach(() => {
  heyUI.$LoadingBar.success()
})

export default router
