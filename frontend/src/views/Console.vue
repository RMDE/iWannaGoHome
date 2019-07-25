<template>
  <div class="console">
    <Header>
      <div v-font="18" class="icon-button">
        <!--        <i class="iconfont icon-menu"></i>-->
        <h4>后台管理</h4>
      </div>
      <div v-font="14" class="icon-button">
        <DropdownMenu @click="onUserClick" :datas="param" trigger="hover" :show-count="true"
                      :width="150">
          <i class="iconfont icon-user"></i>
        </DropdownMenu>
      </div>
    </Header>
    <div class="console-container">
      <ShadowCard class="pc-show tablet-show" :padding="false">
        <div class="console-menu">
          <Menu :datas="data" v-width="75" className="h-menu-white" id="consoleMenu" ref="consoleMenu"
                @select="menuSelect"
                inlineCollapsed v-font="18"></Menu>
        </div>
      </ShadowCard>
      <div class="console-view">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import Header from '../components/Header'
  import ShadowCard from '../components/ShadowCard'
  import { mapMutations } from 'vuex'
  import { delCookie } from '../utils/cookie'

  export default {
    name: 'Console',
    components: {
      Header,
      ShadowCard
    },
    data () {
      return {
        param: [
          { title: '首页', key: 'home', icon: 'h-icon-home' },
          { divider: true },
          { title: '注销', key: 'logout', icon: 'h-icon-outbox', disabled: false }
        ],
        data: [
          {
            title: '系统',
            key: 'consoleSystem',
            icon: 'iconfont icon-all'
          },
          {
            title: '项目',
            key: 'consoleProject',
            icon: 'iconfont icon-project'
          },
          {
            title: 'Mock',
            key: 'consoleMockTable',
            icon: 'iconfont icon-mock'
          },
          {
            title: '用户',
            key: 'consoleUser',
            icon: 'iconfont icon-user-management'
          }
        ]
      }
    },
    methods: {
      onUserClick (code) {
        let goto
        if (code === 'home') {
          goto = '/'
        } else if (code === 'logout') {
          delCookie('token')
          goto = '/'
        }
        this.$router.push(goto)
      },
      ...mapMutations({
        // triggerDrawer: 'system/triggerConsoleDrawer'
      }),
      menuSelect (data) {
        this.$router.push({ name: data.key })
      }
    },
    watch: {
      $route () {
        if (this.$route.name) {
          // router的name与menu的key对应
          this.$refs.consoleMenu.select(this.$route.name)
        }
      }
    }
  }
</script>

<style scoped lang="less">
  .console {
    background-color: @console-bg;
    height: 100%;
  }

  .console-header {
    height: 48px;
    width: 100%;
    box-shadow: @header-shadow;
    position: fixed;
    background-color: white;
    z-index: 999;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .console-container {
    margin-top: 48px;
    max-width: @body-max-width;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    align-items: start;
    justify-content: start;
    flex-direction: row;
    @media screen and (max-width: 425px) {
      margin-top: 36px;
    }
  }

  .console-view {
    flex: 1;
  }

  /deep/ .iconfont {
    font-size: 16px;
  }

</style>
