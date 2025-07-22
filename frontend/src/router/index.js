import { createRouter, createWebHistory } from 'vue-router'
import LoginForm from '@/views/LoginForm.vue'
import CreacionDeCampana from '@/views/CreacionDeCampana.vue'
import MenuPrincipal from '@/views/MenuPrincipal.vue'
import PlantillaVue from '@/views/Plantilla.vue'
import VentanaDePiezas from '@/views/VentanaDePiezas.vue'
import InformeFinanciero from '@/views/InformeFinanciero.vue'
import CrearDashboard from '@/views/CrearDashboard.vue' // <--- AGREGADO
import DetalleCampaña from '@/views/DetalleCampaña.vue'

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
  },
  {
    path: '/informe-financiero',
    name: 'InformeFinanciero',
    component: InformeFinanciero
  },
  {
    path: '/crear-dashboard',             // <--- NUEVA RUTA
    name: 'CrearDashboard',
    component: CrearDashboard
  },
  {
    path: '/detalle-campaña/:slug',       // <--- CAMBIA :nombre por :slug
    name: 'DetalleCampaña',
    component: DetalleCampaña
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
