const path = require('path')
const TerserPlugin = require('terser-webpack-plugin')
const CompressionWebpackPlugin = require('compression-webpack-plugin')

const productionGzipExtensions = /\.(js|css|json|txt|html|ico|svg)(\?.*)?$/i
const isProduction = process.env.NODE_ENV === 'production'
const cdn = {
  css: [],
  js: [
    'https://cdn.bootcss.com/vue/2.6.10/vue.runtime.min.js',
    'https://cdn.bootcss.com/vue-router/3.0.4/vue-router.min.js',
    'https://cdn.bootcss.com/vuex/3.1.0/vuex.min.js',
    'https://cdn.bootcss.com/axios/0.18.0/axios.min.js',
    'https://cdn.bootcss.com/marked/0.6.2/marked.min.js'
  ]
}

function resolve (dir) {
  return path.join(__dirname, dir)
}

module.exports = {
  // 基本路径
  publicPath: '/',
  // 输出文件目录
  outputDir: 'dist',
  assetsDir: '',
  // 放置生成的静态资源 (js、css、img、fonts) 的 (相对于 outputDir 的) 目录。
  // assetsDir: './',
  // 指定生成的 index.html 的输出路径 (相对于 outputDir)。也可以是一个绝对路径
  // indexPath: './',
  // eslint-loader 是否在保存的时候检查
  lintOnSave: true,
  pluginOptions: {
    'style-resources-loader': {
      preProcessor: 'less',
      patterns: [
        path.resolve(__dirname, './src/assets/style/var.less')
      ]
    }
  },
  // webpack配置
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md
  chainWebpack: config => {
    config
      .entry('index')
      .add('@babel/polyfill')
      .end()
    // 配置别名
    config.resolve.alias
      .set('@', resolve('src'))
      .set('@style', resolve('src/assets/style'))
    // 生产环境配置
    if (isProduction) {
      // 删除预加载
      config.plugins.delete('preload')
      config.plugins.delete('prefetch')
      // 压缩代码
      config.optimization.minimize(true)
      // 分割代码
      config.optimization.splitChunks({
        chunks: 'all',
        name: 'vendor'
      })
      // 生产环境注入cdn
      config.plugin('html')
        .tap(args => {
          args[0].cdn = cdn
          return args
        })

      config.optimization.minimizer = [
        new TerserPlugin({
          parallel: true,
          sourceMap: false
        })
      ]
    }
  },
  configureWebpack: config => {
    if (isProduction) {
      // 用cdn方式引入
      config.externals = {
        'vue': 'Vue',
        'vuex': 'Vuex',
        'vue-router': 'VueRouter',
        'axios': 'axios',
        'marked': 'marked'
      }
      // GZip压缩
      const plugins = []
      plugins.push(
        new CompressionWebpackPlugin({
          filename: '[path].gz[query]',
          algorithm: 'gzip',
          test: productionGzipExtensions,
          threshold: 8194,
          minRatio: 0.8
        })
      )
      config.plugins = [
        ...config.plugins,
        ...plugins
      ]
    } else {
      // 为开发环境修改配置...
    }
  },
  // 生产环境是否生成 sourceMap 文件
  productionSourceMap: false,
  // css相关配置
  css: {
    // 是否使用css分离插件 ExtractTextPlugin
    extract: true,
    // 开启 CSS source maps?
    sourceMap: false,
    // css预设器配置项
    loaderOptions: {},
    // 启用 CSS modules for all css / pre-processor files.
    modules: false
  },
  // use thread-loader for babel & TS in production build
  // enabled by default if the machine has more than 1 cores
  parallel: require('os').cpus().length > 1,
  devServer: {
    port: 8080, // 端口
    open: true, // 自动开启浏览器
    compress: false, // 开启压缩
    overlay: {
      warnings: true,
      errors: true
    }
  }
}
