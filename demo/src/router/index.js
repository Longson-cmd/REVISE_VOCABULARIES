import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import WordDetailPage from '../views/WordDetailPage.vue'
import NewWords from '../views/NewWords.vue'
import SelfIntroduction from '../views/SelfIntroduction.vue'


const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/NewWords', name: 'NewWords', component: NewWords },
  { path: '/word/:key', name: 'WordDetailPage', component: WordDetailPage },
  { path: '/self_introduction', name: 'self_introduction', component: SelfIntroduction  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
