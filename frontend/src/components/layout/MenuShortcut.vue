<template>
  <div :class="['menu-shortcut', className]">
    <div :class="['a', divClassName]">{{ shortcut }}</div>
  </div>
</template>

<script>
export default {
  name: "MenuShortcut",
  props: {
    shortcut: {
      type: String,
      default: "⇧A",
    },
    className: {
      type: String,
      default: "",
    },
    divClassName: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.menu-shortcut {
  align-items: center;
  border-radius: 8px;
  display: inline-flex;
  justify-content: flex-end;
  position: relative;
}

.menu-shortcut .a {
  color: var(--color-text-default-default);
  font-family: var(--single-line-body-base-font-family);
  font-size: var(--single-line-body-base-font-size);
  font-style: var(--single-line-body-base-font-style);
  font-weight: var(--single-line-body-base-font-weight);
  letter-spacing: var(--single-line-body-base-letter-spacing);
  line-height: var(--single-line-body-base-line-height);
  margin-top: -1.00px;
  position: relative;
  white-space: nowrap;
  width: fit-content;
}
</style>
