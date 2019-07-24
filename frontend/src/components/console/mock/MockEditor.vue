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
      <FormItem prop="mode">
        <template v-slot:label><i class="iconfont icon-data"></i>图表类型</template>
        <Select v-model="mode" :datas="modes" :multiple="false"></Select>
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
        <Button text-color="blue" icon="iconfont icon-draft">预览</Button>
        <Button color="blue" icon="iconfont icon-save">发 布</Button>
        <Button text-color="blue" icon="iconfont icon-hide">隐藏</Button>
      </ButtonGroup>
    </div>
  </div>
</template>

<script>
  import vueJsonEditor from 'vue-json-editor'
  // import MockApi from '../../../api/mock'

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
        // 项目列表
        projects: [],
        mode: null,
        // 图标类型列表
        modes: []
      }
    },
    created () {
      this.mockId = this.$route.params.mockId
    },
    mounted () {
      if (this.mockId !== null) {
        // MockApi.fetchMock(this.mockId).then((res) => {
        //
        // }).catch((err)=>{
        //
        // })
      }
    },
    methods: {
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
    height: 512px;
    margin: 0 0 0 24px;
  }

  /deep/ .jsoneditor {
    border-radius: 6px;
  }
</style>
