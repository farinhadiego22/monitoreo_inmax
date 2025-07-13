<template>
  <svg
    :class="['size-16-1', className]"
    fill="none"
    height="16"
    viewBox="0 0 16 16"
    width="16"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M7.99992 1.3335L10.0599 5.50683L14.6666 6.18016L11.3333 9.42683L12.1199 14.0135L7.99992 11.8468L3.87992 14.0135L4.66659 9.42683L1.33325 6.18016L5.93992 5.50683L7.99992 1.3335Z"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="1.6"
    />
  </svg>
</template>

<script>
export default {
  name: "Size16_1",
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
