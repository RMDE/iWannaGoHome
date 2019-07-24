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
      <FormItem label="数据" :single="true" prop="textareaData">
        <textarea rows="3" v-autosize v-wordcount="50" v-model="json"></textarea>
      </FormItem>
    </Form>
  </div>
</template>

<script>
  export default {
    name: 'MockEditor',
    data () {
      return {
        mockId: null,
        name: null,
        project: null,
        json: null,
        projects: []
      }
    },
    created () {
      this.mockId = this.$route.params.mockId
    },
    methods: {
      goBack () {
        this.$router.back()
      }
    }
  }
</script>

<style scoped>

</style>
