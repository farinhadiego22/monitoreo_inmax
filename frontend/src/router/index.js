import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '@/views/LoginForm.vue'
import CreacionDeCampana from '@/views/CreacionDeCampana.vue'
import MenuPrincipal from '@/views/MenuPrincipal.vue'
import PlantillaVue from '@/views/Plantilla.vue'
import VentanaDePiezas from '@/views/VentanaDePiezas.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginForm
  },
  {
    path: '/creacion-de-campana',
    name: 'CreacionDeCampana',
    component: CreacionDeCampana
  },
  {
    path: '/menu-principal',
    name: 'MenuPrincipal',
    component: MenuPrincipal
  },
  {
    path: '/plantillavue',
    name: 'PlantillaVue',
    component: PlantillaVue
  },
  {
    path: '/ventana-de-piezas',
    name: 'VentanaDePiezas',
    component: VentanaDePiezas
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
