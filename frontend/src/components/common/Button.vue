<template>
  <button :class="['button', state, variant, className]">
    <div class="text-wrapper">{{ label }}</div>
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    label: {
      type: String,
      default: "Button",
    },
    hasIconEnd: {
      type: Boolean,
      default: false,
    },
    hasIconStart: {
      type: Boolean,
      default: false,
    },
    variant: {
      type: String,
      default: "",
    },
    state: {
      type: String,
      default: "",
    },
    size: {
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
.button {
  all: unset;
  align-items: center;
  border-radius: var(--size-radius-200);
  box-sizing: border-box;
  display: inline-flex;
  gap: var(--size-space-200);
  justify-content: center;
  overflow: hidden;
  padding: var(--size-space-300);
  position: relative;
}

.button .text-wrapper {
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

.button.hover {
  border: 1px solid;
}

.button.primary {
  border: 1px solid;
  border-color: var(--color-border-brand-default);
}

.button.default.primary {
  background-color: var(--color-background-brand-default);
}

.button.hover.subtle {
  border-color: var(--color-border-default-default);
}

.button.hover.primary {
  background-color: var(--color-background-brand-hover);
}

.button.primary .text-wrapper {
  color: var(--color-text-brand-on-brand);
}

.button.default.subtle .text-wrapper {
  color: var(--color-text-neutral-default);
}

.button.hover.subtle .text-wrapper {
  color: var(--color-text-default-default);
}
</style>
