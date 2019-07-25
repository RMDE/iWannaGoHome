<template>
  <div>
    <ShadowCard>
      <div class="console-title">
        <i class="iconfont icon-setting"></i>
        <h3>系统总览</h3>
      </div>
    </ShadowCard>
    <ShadowCard>
      <!--      <h4 class="card-title">集群管理</h4>-->
      <Button color="yellow" icon="iconfont icon-start">启动集群</Button>
      <Button text-color="red" icon="iconfont icon-stop">停止集群</Button>
    </ShadowCard>
  </div>
</template>

<script>
  import ShadowCard from '../ShadowCard'

  export default {
    name: 'SystemConfiguration',
    components: {
      ShadowCard
    }
  }
</script>

<style scoped lang="less">

</style>
