import axios from 'axios'
import user from '@/store/modules/user'
import Vue from 'vue'
import baseUrl from './base'

// 创建axios实例
const instance = axios.create({
  timeout: 1000 * 12,
  baseURL: baseUrl
})

// 设置post请求头
instance.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'

instance.interceptors.request.use(
  config => {
    const token = user.getters.token()
    config.headers = {
      'Content-Type': 'application/json' // 设置跨域头部
    }
    // 时刻携带token
    config.auth = { username: token, password: null }
    // 加个时间戳使得浏览器不使用缓存，重新请求api
    if (config.url.indexOf(baseUrl.vuebee) >= 0) {
      config.url += '?time=' + (new Date()).valueOf()
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

instance.interceptors.response.use(
  data => {
    console.log(data)
    return data
  },
  err => {
    console.log(err)
    if (err.response.status === 504 || err.response.status === 502) {
      Vue.prototype.$Notice['error']('服务器挂了')
    } else {
      // 直接显示API返回的错误信息
      Vue.prototype.$Notice['error'](err.response.data['msg'])
    }
    return Promise.reject(err)
  }
)
export default instance
