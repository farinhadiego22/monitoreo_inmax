<script setup>
import { ref } from 'vue'
import api from '../axios'

const email = ref('')
const password = ref('')
const error = ref(null)
const user = ref(null)

const login = async () => {
  try {
    const res = await api.post('/auth/login', {
      email: email.value,
      password: password.value,
    })
    localStorage.setItem('token', res.data.access_token)

    const me = await api.get('/auth/me')
    user.value = me.data
    error.value = null
  } catch (err) {
    error.value = 'Credenciales incorrectas'
  }
}
</script>
  
<template>
  <form @submit.prevent="login">
    <input v-model="email" placeholder="Correo" />
    <input v-model="password" type="password" placeholder="Contraseña" />
    <button type="submit">Entrar</button>

    <p v-if="error" style="color: red;">{{ error }}</p>
    <p v-if="user" style="margin-top: 1rem;">Bienvenido, {{ user.email }}</p>
  </form>
</template>
