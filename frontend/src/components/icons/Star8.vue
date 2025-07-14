<template>
  <svg
    :class="['star-8', className]"
    fill="none"
    height="20"
    viewBox="0 0 20 20"
    width="20"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M10 1.66666L12.575 6.88333L18.3333 7.725L14.1667 11.7833L15.15 17.5167L10 14.8083L4.85001 17.5167L5.83334 11.7833L1.66667 7.725L7.425 6.88333L10 1.66666Z"
      :stroke="color"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
    />
  </svg>
</template>

<script>
export default {
  name: "Star8",
  props: {
    color: {
      type: String,
      default: "#1E1E1E",
    },
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>
