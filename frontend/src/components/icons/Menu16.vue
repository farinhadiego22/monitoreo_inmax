<template>
  <svg
    :class="['menu-16', className]"
    fill="none"
    height="16"
    viewBox="0 0 16 16"
    width="16"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      class="path"
      clip-rule="evenodd"
      d="M1.25 4C1.25 3.58579 1.58579 3.25 2 3.25H14C14.4142 3.25 14.75 3.58579 14.75 4C14.75 4.41421 14.4142 4.75 14 4.75H2C1.58579 4.75 1.25 4.41421 1.25 4ZM1.25 8C1.25 7.58579 1.58579 7.25 2 7.25H14C14.4142 7.25 14.75 7.58579 14.75 8C14.75 8.41421 14.4142 8.75 14 8.75H2C1.58579 8.75 1.25 8.41421 1.25 8ZM1.25 12C1.25 11.5858 1.58579 11.25 2 11.25H14C14.4142 11.25 14.75 11.5858 14.75 12C14.75 12.4142 14.4142 12.75 14 12.75H2C1.58579 12.75 1.25 12.4142 1.25 12Z"
      fill="#1E1E1E"
      fill-rule="evenodd"
    />
  </svg>
</template>

<script>
export default {
  name: "Menu16",
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
