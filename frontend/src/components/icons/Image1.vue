<template>
  <svg
    :class="['image-1', className]"
    fill="none"
    height="39"
    viewBox="0 0 43 39"
    width="43"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      d="M8.95833 34.125H34.0417C36.0207 34.125 37.625 32.6699 37.625 30.875V8.125C37.625 6.33007 36.0207 4.875 34.0417 4.875H8.95833C6.97931 4.875 5.375 6.33007 5.375 8.125V30.875C5.375 32.6699 6.97931 34.125 8.95833 34.125ZM8.95833 34.125L28.6667 16.25L37.625 24.375M17.9167 13.8125C17.9167 15.1587 16.7134 16.25 15.2292 16.25C13.7449 16.25 12.5417 15.1587 12.5417 13.8125C12.5417 12.4663 13.7449 11.375 15.2292 11.375C16.7134 11.375 17.9167 12.4663 17.9167 13.8125Z"
      stroke="#1E1E1E"
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="4"
    />
  </svg>
</template>

<script>
export default {
  name: "Image1",
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
