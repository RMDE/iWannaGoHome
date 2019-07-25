<template>
  <ShadowCard>
    <div class="console-title">
      <i class="iconfont icon-management"></i>
      <h3>项目管理</h3>
    </div>
    <router-view></router-view>
  </ShadowCard>
</template>

<script>
  import ShadowCard from '../../ShadowCard'

  export default {
    name: 'ProjectManagement',
    components: {
      ShadowCard
    }
  }
</script>

<style scoped>

</style>
