<template>
  <div :class="['text-link', className]">
    <div class="div">{{ text }}</div>
  </div>
</template>

<script>
export default {
  name: "TextLink",
  props: {
    text: {
      type: String,
      default: "Text Link",
    },
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.text-link {
  align-items: flex-start;
  display: inline-flex;
  position: relative;
}

.text-link .div {
  color: var(--color-text-default-default);
  font-family: var(--body-link-font-family);
  font-size: var(--body-link-font-size);
  font-style: var(--body-link-font-style);
  font-weight: var(--body-link-font-weight);
  letter-spacing: var(--body-link-letter-spacing);
  line-height: var(--body-link-line-height);
  margin-top: -1.00px;
  position: relative;
  text-decoration: underline;
  white-space: nowrap;
  width: fit-content;
}
</style>
