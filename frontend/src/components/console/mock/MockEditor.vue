<template>
  <div>
    <p class="console-buttons">
      <Button size="s" text-color="blue" icon="iconfont icon-goback" @click="goBack">返回</Button>
    </p>
    <Form ref="form" mode="single" :label-width="100">
      <FormItem prop="name">
        <template v-slot:label><i class="iconfont icon-title"></i>名称</template>
        <input type="text" v-model="name">
      </FormItem>
      <FormItem prop="project">
        <template v-slot:label><i class="iconfont icon-category"></i>所属项目</template>
        <Select v-model="project" :datas="projects" :multiple="false"></Select>
      </FormItem>
      <FormItem prop="form">
        <template v-slot:label><i class="iconfont icon-data"></i>图表类型</template>
        <Select v-model="form" :datas="forms" :multiple="false"></Select>
      </FormItem>
      <FormItem :single="true" prop="textareaData">
        <template v-slot:label><i class="iconfont icon-post"></i>描述</template>
        <textarea rows="3" v-autosize v-wordcount="1024" v-model="desc"></textarea>
      </FormItem>
    </Form>
    <vue-json-editor v-model="json"
                     :show-btns="false"
                     :mode="'code'"
                     lang="zh"
                     height="400px"
                     @json-change="onJsonChange"
                     @json-save="onJsonSave"
                     @has-error="onError">
    </vue-json-editor>
    <div class="post-editor-bottom">
      <ButtonGroup :circle="false" size="s">
        <Button text-color="blue" icon="iconfont icon-draft">图表预览</Button>
        <Button color="blue" icon="iconfont icon-save" @click="submit">发 布</Button>
        <Button text-color="blue" icon="iconfont icon-hide" @click="abandon">废弃</Button>
      </ButtonGroup>
    </div>
  </div>
</template>

<script>
  import vueJsonEditor from 'vue-json-editor'
  import MockApi from '../../../api/mock'
  import { mapActions } from 'vuex'

  export default {
    name: 'MockEditor',
    components: {
      vueJsonEditor
    },
    data () {
      return {
        mockId: null,
        name: null,
        project: null,
        json: null,
        desc: null,
        // 项目列表
        projects: [],
        form: null,
        // 图标类型列表
        forms: [
          '折线图',
          '柱状图',
          '条形图',
          '饼图',
          '环图',
          '瀑布图',
          '漏斗图',
          '雷达图',
          '地图',
          '桑基图',
          '热力图',
          '散点图',
          'K线图',
          '仪表盘',
          '树图',
          '水球图',
          '词云图'
        ]
      }
    },
    created () {
      this.mockId = this.$route.params.mockId
    },
    mounted () {
      if (this.mockId !== null && this.mockId !== undefined) {
        this.$Loading()
        MockApi.fetchMock(this.mockId).then((res) => {
          // 解构赋值
          let jsonRaw
          ({
            name: this.name,
            json: jsonRaw,
            project: this.project,
            form: this.form,
            projects: this.projects
          } = res.data)
          this.json = JSON.parse(jsonRaw)
        }).catch(() => {
          this.$Notice['error']('数据加载错误')
        }).finally(() => {
          this.$Loading.close()
        })
      }
    },
    methods: {
      ...mapActions({
        createMock: 'mock/createMock',
        updateMock: 'mock/updateMock',
        abandonMock: 'mock/abandonMock'
      }),
      goBack () {
        this.$router.back()
      },
      onJsonChange (value) {
        console.log('value:', value)
      },
      onJsonSave (value) {
        console.log('value:', value)
      },
      onError (value) {
        console.log('value:', value)
      },
      submit () {
        let mock = {
          name: this.name,
          project: this.project,
          json: JSON.stringify(this.json),
          desc: this.desc,
          form: this.form
        }
        console.log(mock)

        let result

        if (this.mockId !== null && this.mockId !== undefined) {
          // 修改
          result = this.updateMock({ id: this.mockId, mock: mock })
        } else {
          // 新增
          result = this.createMock(mock)
        }

        if (result) {
          setTimeout(() => {
            this.$router.back()
          }, 1000)
        }
      },
      abandon () {
        if (this.mockId !== undefined && this.mockId !== null) {
          let result = this.abandonMock(this.mockId)
          if (result) {
            setTimeout(() => {
              this.$router.back()
            }, 1000)
          }
        }
      }
    }
  }
</script>

<style scoped>
  .post-editor-bottom {
    margin-top: 12px;
    text-align: right;
    margin-bottom: 4px;
  }

  /deep/ .jsoneditor-vue {
    height: 480px;
    margin: 0 0 0 24px;
  }

  /deep/ .jsoneditor {
    border-radius: 6px;
  }
</style>
