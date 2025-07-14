<template>
  <div :class="['select-field', className]">
    <div v-if="hasLabel" class="label">{{ label }}</div>
    <div class="select">
      <div class="value">{{ value }}</div>
      <Size16_2 class="chevron-down" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Size16_2 from "../icons/Size16_2.vue";

export default defineComponent({
  name: "SelectField",
  components: {
    Size16_2
  },
  props: {
    hasLabel: {
      type: Boolean,
      default: true,
    },
    hasError: {
      type: Boolean,
      default: true,
    },
    label: {
      type: String,
      default: "Label",
    },
    error: {
      type: String,
      default: "Error",
    },
    open: {
      type: Boolean,
      default: false,
    },
    description: {
      type: String,
      default: "Description",
    },
    hasDescription: {
      type: Boolean,
      default: false,
    },
    value: {
      type: String,
      default: "Value",
    },
    state: {
      type: String,
    },
    valueType: {
      type: String,
    },
    className: {
      type: String,
      default: "",
    },
  },
});
</script>

<style>
.select-field {
  align-items: flex-start;
  display: inline-flex;
  flex-direction: column;
  gap: var(--size-space-200);
  position: relative;
}

.select-field .label {
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

.select-field .select {
  align-items: center;
  align-self: stretch;
  background-color: var(--color-background-default-default);
  border: 1px solid;
  border-color: var(--color-border-default-default);
  border-radius: var(--size-radius-200);
  display: flex;
  gap: var(--size-space-200);
  height: 42px;
  margin-bottom: -1.00px;
  margin-left: -1.00px;
  margin-right: -1.00px;
  min-width: 240px;
  padding: var(--size-space-300) var(--size-space-300) var(--size-space-300)
    var(--size-space-400);
  position: relative;
  width: 100%;
}

.select-field .value {
  color: var(--color-text-default-default);
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

.select-field .chevron-down {
  height: 16px !important;
  position: relative !important;
  width: 16px !important;
}
</style>
