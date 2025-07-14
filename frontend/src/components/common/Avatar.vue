<template>
  <div :class="['avatar', className]" />
</template>

<script>
export default {
  name: "Avatar",
  props: {
    initials: {
      type: String,
      default: "F",
    },
    type: {
      type: String,
      default: "",
    },
    size: {
      type: String,
      default: "",
    },
    shape: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.avatar {
  background-image: url(https://c.animaapp.com/DL5zdupI/img/shape-2@2x.png);
  background-position: 50% 50%;
  background-size: cover;
  border-radius: var(--size-radius-full);
  height: var(--size-icon-large);
  width: var(--size-icon-large);
}
</style>
