<template>
  <div :class="['menu-separator', className]">
    <div class="rule" />
  </div>
</template>

<script>
export default {
  name: "MenuSeparator",
  props: {
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.menu-separator {
  align-items: center;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: var(--size-padding-sm) var(--size-padding-lg) var(--size-padding-sm) var(--size-padding-lg);
  position: relative;
  width: 284px;
}

.menu-separator .rule {
  align-self: stretch;
  background-color: var(--color-border-default-default);
  height: 1px;
  position: relative;
  width: 100%;
}
</style>
