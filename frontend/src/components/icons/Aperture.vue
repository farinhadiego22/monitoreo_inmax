<template>
  <svg
    :class="['aperture', className]"
    fill="none"
    height="48"
    viewBox="0 0 48 48"
    width="48"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M28.62 16L40.1 35.88M19.38 16H42.34M14.76 24L26.24 4.12M19.38 32L7.9 12.12M28.62 32H5.66M33.24 24L21.76 43.88M44 24C44 35.0457 35.0457 44 24 44C12.9543 44 4 35.0457 4 24C4 12.9543 12.9543 4 24 4C35.0457 4 44 12.9543 44 24Z"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="4"
    />
  </svg>
</template>

<script>
export default {
  name: "Aperture",
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
