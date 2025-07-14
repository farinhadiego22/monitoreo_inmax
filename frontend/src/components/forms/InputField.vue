<template>
  <div :class="['input-field', className]">
    <div v-if="hasLabel" class="label">{{ label }}</div>
    <div class="input">
      <div class="value">{{ value }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InputField",
  props: {
    hasLabel: {
      type: Boolean,
      default: true,
    },
    hasError: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
      default: "Label",
    },
    error: {
      type: String,
      default: "Error",
    },
    hasDescription: {
      type: Boolean,
      default: false,
    },
    description: {
      type: String,
      default: "Description",
    },
    value: {
      type: String,
      default: "Value",
    },
    state: {
      type: String,
      default: "",
    },
    valueType: {
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
.input-field {
  align-items: flex-start;
  display: inline-flex;
  flex-direction: column;
  gap: var(--size-space-200);
  position: relative;
}

.input-field .label {
  align-self: stretch;
  color: var(--color-text-default-default);
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  margin-top: -1.00px;
  position: relative;
}

.input-field .input {
  align-items: center;
  align-self: stretch;
  background-color: var(--color-background-default-default);
  border: 1px solid;
  border-color: var(--color-border-default-default);
  border-radius: var(--size-radius-200);
  display: flex;
  flex: 0 0 auto;
  margin-bottom: -1.00px;
  margin-left: -1.00px;
  margin-right: -1.00px;
  min-width: 240px;
  overflow: hidden;
  padding: var(--size-space-300) var(--size-space-400) var(--size-space-300)
    var(--size-space-400);
  position: relative;
  width: 100%;
}

.input-field .value {
  color: var(--color-text-default-tertiary);
  flex: 1;
  font-family: var(--single-line-body-base-font-family);
  font-size: var(--single-line-body-base-font-size);
  font-style: var(--single-line-body-base-font-style);
  font-weight: var(--single-line-body-base-font-weight);
  letter-spacing: var(--single-line-body-base-letter-spacing);
  line-height: var(--single-line-body-base-line-height);
  margin-top: -0.50px;
  position: relative;
}
</style>
