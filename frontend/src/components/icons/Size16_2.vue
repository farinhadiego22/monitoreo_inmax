<template>
  <svg
    :class="['size-16-2', className]"
    fill="none"
    height="16"
    viewBox="0 0 16 16"
    width="16"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M4 6L8 10L12 6"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="1.6"
    />
  </svg>
</template>

<script>
export default {
  name: "Size16_2",
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
