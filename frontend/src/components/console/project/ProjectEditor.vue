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
      <FormItem :single="true" prop="textareaData">
        <template v-slot:label><i class="iconfont icon-post"></i>描述</template>
        <textarea rows="3" v-autosize v-wordcount="1024" v-model="desc"></textarea>
      </FormItem>
    </Form>
    <mavon-editor :boxShadow="false" :subfield="false" v-model="markdown" :toolbars="toolbars"></mavon-editor>
    <div class="post-editor-bottom">
      <ButtonGroup :circle="false" size="s">
        <!--        <Button text-color="blue" icon="iconfont icon-draft">预览</Button>-->
        <Button color="blue" icon="iconfont icon-save" @click="submit">发 布</Button>
        <!--        <Button text-color="blue" icon="iconfont icon-hide">隐藏</Button>-->
      </ButtonGroup>
    </div>
  </div>
</template>

<script>
  import ProjectApi from '../../../api/project'
  import { mavonEditor } from 'mavon-editor'
  import { mapActions } from 'vuex'

  export default {
    name: 'ProjectEditor',
    components: {
      mavonEditor
    },
    data () {
      return {
        projectId: null,
        name: null,
        desc: null,
        markdown: '',
        toolbars: {
          bold: true, // 粗体
          italic: true, // 斜体
          header: true, // 标题
          underline: true, // 下划线
          strikethrough: true, // 中划线
          mark: true, // 标记
          superscript: true, // 上角标
          subscript: true, // 下角标
          quote: true, // 引用
          ol: true, // 有序列表
          ul: true, // 无序列表
          link: true, // 链接
          imagelink: true, // 图片链接
          code: true, // code
          table: true, // 表格
          fullscreen: true, // 全屏编辑
          readmodel: true, // 沉浸式阅读
          htmlcode: true, // 展示html源码
          help: false, // 帮助
          /* 1.3.5 */
          undo: true, // 上一步
          redo: true, // 下一步
          trash: true, // 清空
          save: true, // 保存（触发events中的save事件）
          /* 1.4.2 */
          navigation: false, // 导航目录
          /* 2.1.8 */
          alignleft: true, // 左对齐
          aligncenter: true, // 居中
          alignright: true, // 右对齐
          /* 2.2.1 */
          subfield: true, // 单双栏模式
          preview: true // 预览
        }
      }
    },
    created () {
      this.projectId = this.$route.params.projectId
    },
    mounted () {
      if (this.projectId !== null && this.projectId !== undefined) {
        this.$Loading()
        ProjectApi.fetchProject(this.projectId).then((res) => {
          ({
            name: this.name,
            desc: this.desc,
            markdown: this.markdown
          } = res.data)
        }).catch((e) => {
          console.log(e)
        }).finally(() => {
          this.$Loading.close()
        })
      }
    },
    methods: {
      ...mapActions({
        createProject: 'project/createProject',
        updateProject: 'project/updateProject'
      }),
      goBack () {
        this.$router.back()
      },
      submit () {
        let project = {
          name: this.name,
          desc: this.desc,
          markdown: this.markdown
        }

        let result

        if (this.projectId !== null && this.projectId !== undefined) {
          // 更新
          result = this.updateProject({ id: this.projectId, project: project })
        } else {
          // 新增
          result = this.createProject(project)
        }

        if (result) {
          setTimeout(() => {
            this.$router.back()
          }, 1000)
        }
      }
    }
  }
</script>

<style scoped lang="less">
  .post-editor-bottom {
    margin-top: 12px;
    text-align: right;
    margin-bottom: 4px;
  }

  /deep/ .markdown-body {
    @import "~mavon-editor/dist/css/index.css";

    z-index: 999 !important;

    .popup-dropdown {
      box-shadow: 0 0 4px 0 rgba(0, 21, 41, .18) !important;
      border-radius: 6px;
    }

    .input-wrapper {
      border: none !important;

      input {
        border: 1px solid #eee !important;
      }

      input:focus {
        border-color: @a-hover-color !important;
      }
    }

    .content-input-wrapper, .v-note-show {
      min-height: 360px !important;
      max-height: 576px !important;
    }

    .add-image-link {
      padding: 18px !important;

      .title {
        margin: 12px !important;
      }

      i.fa {
        display: none;
      }

      .op-btn {
        outline: none !important;
        display: inline-block;
        border-radius: 4px !important;
        color: inherit;
        font-size: 13px !important;
        line-height: 1;
        box-sizing: border-box;
        cursor: pointer;
        transition: all .2s;
        border: 1px solid #d3d3d3;
        box-shadow: 0 1px 1px 0 #eee;
        background-color: #fff;
        margin-top: 20px !important;
      }

      .sure {
        background-color: @blue-color !important;
      }

      .cancel {
        background-color: @secondary-text-color !important;
        color: white !important;

        :hover {
          color: white !important;
        }
      }

      .input-wrapper {
        margin: 12px 0 0 0 !important;
        width: 100% !important;

        input {
          margin: auto 0 !important;
          width: 100% !important;
        }
      }
    }

    // 编辑器textarea阴影
    .auto-textarea-wrapper textarea:focus {
      box-shadow: none;
    }
  }

  // 编辑器一些按钮外观
  /deep/ .markdown-body [type='button'] {
    -webkit-appearance: none;
  }
</style>
