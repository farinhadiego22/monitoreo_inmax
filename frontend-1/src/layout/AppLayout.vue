<template>
  <div>
    <header>
      <h1>Application Header</h1>
    </header>
    <main>
      <slot />
    </main>
    <footer>
      <p>Application Footer</p>
    </footer>
  </div>
</template>

<script setup>
</script>

<style scoped>
header {
  background-color: #f8f9fa;
  padding: 20px;
  text-align: center;
}

main {
  padding: 20px;
}

footer {
  background-color: #f8f9fa;
  padding: 10px;
  text-align: center;
}
</style>