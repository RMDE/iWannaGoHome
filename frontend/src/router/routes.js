import Home from '@/views/Home.vue'

// 定义路由
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "login" */ '@/views/Login.vue')
  },
  {
    path: '/console',
    name: 'console',
    component: () => import(/* webpackChunkName: "console" */'@/views/Console.vue'),
    children: [
      {
        path: 'system',
        meta: { needLogin: true },
        name: 'consoleSystem',
        component: () => import(/* webpackChunkName: "console.system" */'../components/console/System.vue')
      },
      {
        path: 'project',
        meta: { needLogin: true },
        name: 'consoleProject',
        component: () => import(/* webpackChunkName: "console.project" */'../components/console/Project.vue')
      },
      {
        path: 'mock',
        meta: { needLogin: true },
        name: 'consoleMock',
        component: () => import(/* webpackChunkName: "console.mock" */'../components/console/mock/MockManagement.vue'),
        children: [
          {
            path: '',
            meta: { needLogin: true },
            name: 'consoleMockTable',
            component: () => import(/* webpackChunkName: "console.user" */'../components/console/mock/MockTable.vue')
          },
          {
            path: 'edit/:mockId',
            meta: { needLogin: true },
            name: 'consoleMockEditor',
            props: true,
            component: () => import(/* webpackChunkName: "console.user" */'../components/console/mock/MockEditor.vue')
          },
          {
            path: 'edit/new',
            name: 'consoleNewMock',
            props: true,
            component: () => import(/* webpackChunkName: "console.user" */'../components/console/mock/MockEditor.vue')
          }
        ]
      },
      {
        path: 'user',
        meta: { needLogin: true },
        name: 'consoleUser',
        component: () => import(/* webpackChunkName: "console.user" */'../components/console/User.vue')
      }
    ]
  }
]

export default routes
