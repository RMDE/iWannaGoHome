<template>
  <div>
    <ShadowCard>
      <div class="console-title">
        <i class="iconfont icon-data"></i>
        <h3>数据管理</h3>
      </div>
      <p>
        <Button color="blue" icon="h-icon-plus">新建</Button>
        <Button text-color="red" icon="h-icon-trash">删除</Button>
      </p>
    </ShadowCard>
  </div>
</template>

<script>
  import ShadowCard from '../ShadowCard'

  export default {
    name: 'Mock',
    components: {
      ShadowCard
    }
  }
</script>

<style scoped>

</style>
