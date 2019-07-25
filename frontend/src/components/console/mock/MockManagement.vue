<template>
  <ShadowCard>
    <div class="console-title">
      <i class="iconfont icon-data"></i>
      <h3>数据管理</h3>
    </div>

    <router-view></router-view>
  </ShadowCard>
</template>

<script>
  import ShadowCard from '../../ShadowCard'

  export default {
    name: 'MockManagement',
    components: {
      ShadowCard
    }
  }
</script>

<style scoped>

</style>
