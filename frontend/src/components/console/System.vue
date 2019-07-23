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
      <Button color="green"><i class="iconfont icon-start"></i><span>启动集群</span></Button>
      <Button color="red"><i class="iconfont icon-stop"></i><span>停止集群</span></Button>
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

  /deep/ .h-btn span {
    /*font-size: 16px;*/
    /*margin: 0 4px;*/
  }
</style>
