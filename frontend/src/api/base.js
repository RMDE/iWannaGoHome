let baseUrl

if (process.env.NODE_ENV === 'production') {
  baseUrl = '//api.sudocs.com/v1'
} else {
  // 开发环境
  baseUrl = '//localhost:5000/v1'
}

export default baseUrl
