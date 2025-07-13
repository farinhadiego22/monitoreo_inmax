<template>
  <form class="login-form" @submit.prevent="handleSubmit">
    <div class="form-group">
      <label for="username">Username</label>
      <input type="text" id="username" v-model="username" required />
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" id="password" v-model="password" required />
    </div>
    <button type="submit">Login</button>
  </form>
</template>

<script setup>
import { ref } from 'vue';

const username = ref('');
const password = ref('');

const handleSubmit = () => {
  // Handle login logic here
  console.log('Username:', username.value);
  console.log('Password:', password.value);
};
</script>

<style scoped>
.login-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>