<template>
  <svg
    :class="['size-16', className]"
    fill="none"
    height="16"
    viewBox="0 0 16 16"
    width="16"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M12 4L4 12M4 4L12 12"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="1.6"
    />
  </svg>
</template>

<script>
export default {
  name: "Size16",
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
