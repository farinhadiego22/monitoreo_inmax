<template>
  <svg
    :class="['size-48', className]"
    fill="none"
    height="48"
    viewBox="0 0 48 48"
    width="48"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M6 24H42M6 12H42M6 36H42"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="4"
    />
  </svg>
</template>

<script>
export default {
  name: "Size48",
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
