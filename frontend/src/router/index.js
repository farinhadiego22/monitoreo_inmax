import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/LoginForm.vue'
const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  // Aquí agregamos el componenete de registro (Login.vue)
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})