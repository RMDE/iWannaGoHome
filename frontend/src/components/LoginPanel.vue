<template>
  <div class="login-container" @keyup.enter="submit">
    <div class="login-panel">
      <div class="h-panel">
        <div class="h-panel-bar">
          <span class="h-panel-title">登录</span>
          <span class="h-panel-right"><router-link :to="{ name: 'home'}">返回</router-link></span>
        </div>
        <div class="h-panel-body">
          <Form :label-width="60">
            <FormItem label="邮箱">
              <input type="text" v-model="email"/>
            </FormItem>
            <FormItem label="密码">
              <input type="password" v-model="password"/>
            </FormItem>
            <FormItem :no-padding="true">
              <Button color="primary" @click="submit">提交</Button>
              <Button @click="clearInput">重置</Button>
            </FormItem>
          </Form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'LoginPanel',
    data () {
      return {
        email: null,
        password: null
      }
    },
    methods: {
      clearInput: function () {
        this.email = null
        this.password = null
      },
      submit: function () {
        if (this.email == null || this.password == null) {
          // 检查信息输入
          this.$Message({ type: 'error', text: '请输入邮箱和密码' })
        } else {
          // 信息输入正确，请求接口
          this.$Loading()
          this.$LoadingBar.start()
          // 重置登录状态
          this.$store.commit('user/setStatus', 0)
          this.$store.dispatch('user/login', { email: this.email, password: this.password })
        }
      }
    },
    computed: {
      status () {
        return this.$store.getters['user/status']
      }
    },
    watch: {
      // 监控登录状态
      status (update) {
        if (update === 1) {
          this.$Notice['success']('登录成功')
          this.$LoadingBar.success()
          // setTimeout(() => {
          //   this.$router.push({ name: 'consoleIndex' })
          // }, 1000)
        } else if (update === -1) {
          this.$Notice['error']('邮箱或密码错误')
          this.$LoadingBar.fail()
        }
        this.$Loading.close()
      }
    }
  }
</script>

<style scoped lang="less">
  .login-container {
    max-width: @body-max-width;
    margin: 144px auto 0;

    @media screen and(max-width: 425px) {
      margin-top: 72px;
    }
  }

  .login-panel {
    max-width: 425px;
    margin: 0 auto;
    box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);
  }
</style>
