<template>
  <div :class="['navigation-pill', state, className]">
    <div :class="['title', titleClassName]">{{ label }}</div>
  </div>
</template>

<script>
export default {
  name: "NavigationPill",
  props: {
    label: {
      type: String,
      default: "Link",
    },
    state: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
    titleClassName: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.navigation-pill {
  align-items: center;
  border-radius: var(--size-radius-200);
  display: inline-flex;
  gap: var(--size-space-200);
  justify-content: center;
  padding: var(--size-space-200);
  position: relative;
}

.navigation-pill .title {
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

.navigation-pill.active {
  background-color: var(--color-background-brand-tertiary);
}

.navigation-pill.active .title {
  color: var(--color-text-brand-on-brand-secondary);
}

.navigation-pill.default .title {
  color: var(--color-text-default-default);
}
</style>
