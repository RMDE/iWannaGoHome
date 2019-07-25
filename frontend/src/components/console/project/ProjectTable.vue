<template>
  <div>
    <ShadowCard>
      <div class="console-title">
        <i class="iconfont icon-management"></i>
        <h3>项目管理</h3>
      </div>
      <p>
        <Button color="blue" icon="h-icon-plus">新建</Button>
        <Button text-color="red" icon="h-icon-trash">删除</Button>
      </p>
      <Table :datas="projects" :border="true" checkbox :loading="loading" @select="onSelect"
             @trdblclick="onTrDoubleClick">
        <TableItem title="序号" :tooltip="true">
          <template slot-scope="{index}">{{index}}</template>
        </TableItem>
        <TableItem title="id" prop="id" sort="auto"></TableItem>
        <TableItem title="项目名称" align="auto" prop="name" sort="auto"></TableItem>
        <TableItem title="创建时间" align="auto" prop="create_time" sort="auto"></TableItem>
        <TableItem title="更新时间" align="auto" prop="update_time" sort="auto"></TableItem>
        <div slot="empty">暂无数据，赶快添加一个吧</div>
      </Table>
      <div class="space"></div>
      <Pagination v-model="pagination" align="center" @change="currentChange"></Pagination>
    </ShadowCard>
  </div>
</template>

<script>
  import ShadowCard from '../ShadowCard'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'Project',
    components: {
      ShadowCard
    },
    data () {
      return {
        loading: true,
        selected: [],
        // 分页
        pagination: {
          page: 1,
          size: 10,
          total: null
        }
      }
    },
    mounted () {
      this.requestProjects()
    },
    methods: {
      ...mapActions({
        requestProjects: 'project/getProjectList'
      }),
      onSelect (selected) {
        // 传入的是一个列表
        this.selected = []
        selected.forEach((mock) => {
          this.selected.push(mock.id)
        })
      },
      onTrDoubleClick (mock) {
        console.log(mock)
        // this.$router.push({ name: 'consoleMockEditor', params: { mockId: mock.id } })
      },
      currentChange (value) {
        console.log(value)
      }
    },
    computed: {
      ...mapGetters({
        projects: 'project/projects',
        status: 'project/status'
      })
    },
    watch: {
      status (update) {
        this.loading = false
        if (update === 1) {
          this.pagination.total = this.mocks.length
          this.$Message({ type: 'success', text: '项目数据加载完毕' })
        } else if (update === -1) {
          this.$Message({ type: 'error', text: '数据加载发生错误' })
        }
      }
    }
  }
</script>

<style scoped lang="less">
  /deep/ tr {
    cursor: pointer;
  }
</style>
