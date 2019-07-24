<template>
  <div>
    <p>
      <Button color="blue" icon="h-icon-plus" @click="newMock">新建</Button>
      <Button text-color="red" icon="h-icon-trash">删除</Button>
    </p>
    <Table :datas="mocks" :border="true" checkbox :loading="loading" @select="onSelect" @trdblclick="onTrDoubleClick">
      <TableItem title="序号" :tooltip="true">
        <template slot-scope="{index}">{{index}}</template>
      </TableItem>
      <TableItem title="id" prop="id" sort="auto"></TableItem>
      <TableItem title="名称" prop="name"></TableItem>
      <TableItem title="创建者" align="auto" prop="user"></TableItem>
      <TableItem title="所属项目" align="auto" prop="project"></TableItem>
      <TableItem title="创建时间" align="auto" prop="create_time"></TableItem>
      <TableItem title="更新时间" align="auto" prop="update_time"></TableItem>
      <div slot="empty">暂无数据，赶快添加一个吧</div>
    </Table>
    <div class="space"></div>
    <Pagination v-model="pagination" align="center" @change="currentChange"></Pagination>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'MockTable',
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
      this.requestMocks()
    },
    methods: {
      ...mapActions({
        requestMocks: 'mock/getMockList'
      }),
      onSelect (selected) {
        // 传入的是一个列表
        this.selected = []
        selected.forEach((mock) => {
          this.selected.push(mock.id)
        })
      },
      onTrDoubleClick (mock) {
        this.$router.push({ name: 'consoleMockEditor', params: { mockId: mock.id } })
      },
      currentChange (value) {
        console.log(value)
      },
      newMock () {
        this.$router.push({ name: 'consoleNewMock' })
      }
    },
    computed: {
      ...mapGetters({
        mocks: 'mock/mocks',
        mocksStatus: 'mock/mocksStatus'
      })
    },
    watch: {
      mocksStatus (update) {
        this.loading = false
        if (update === 1) {
          this.pagination.total = this.mocks.length
          this.$Message({ type: 'success', text: 'Mock 数据加载完毕' })
        } else if (update === -1) {
          this.$Message({ type: 'error', text: 'Mock 数据加载发生错误' })
        }
      }
    }
  }
</script>

<style scoped>
  .space {
    height: 12px;
  }

  /deep/ tr {
    cursor: pointer;
  }
</style>
