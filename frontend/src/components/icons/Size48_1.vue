<template>
  <svg
    :class="['size-48-1', className]"
    fill="none"
    height="48"
    viewBox="0 0 48 48"
    width="48"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M10 42H38C40.2091 42 42 40.2091 42 38V10C42 7.79086 40.2091 6 38 6H10C7.79086 6 6 7.79086 6 10V38C6 40.2091 7.79086 42 10 42ZM10 42L32 20L42 30M20 17C20 18.6569 18.6569 20 17 20C15.3431 20 14 18.6569 14 17C14 15.3431 15.3431 14 17 14C18.6569 14 20 15.3431 20 17Z"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="4"
    />
  </svg>
</template>

<script>
export default {
  name: "Size48_1",
  props: {
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>
