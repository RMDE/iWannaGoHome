<template>
  <div class="home">
    <Header>
      <h1 class="header-title">
        <router-link to="/">大数据分析展示平台</router-link>
      </h1>
      <div v-font="18" class="icon-button">
        <router-link to="/login"><i class="iconfont icon-user"></i></router-link>
      </div>
    </Header>
  </div>
</template>

<script>
  import Header from '../components/Header'

  export default {
    name: 'home',
    components: {
      Header
    }
  }
</script>

<style scoped lang="less">
  .icon-button /deep/ .iconfont {
    font-size: 20px;
  }

  /deep/ .header-title {
    font-weight: normal;
  }
</style>
