import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { router } from './router' // 👈 Importa tu router

createApp(App)
  .use(router)
  .mount('#app')
