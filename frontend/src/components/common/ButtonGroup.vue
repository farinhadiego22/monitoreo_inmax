<template>
  <div :class="['button-group', className]">
    <Button
      v-if="buttonStart"
      class="button-instance"
      label="Button"
      size="medium"
      state="default"
      variant="subtle"
    />
    <Button
      v-if="buttonEnd"
      class="button-instance"
      :label="buttonLabel"
      size="medium"
      state="default"
      variant="primary"
      @click="$emit('main-click')" 
    />
  </div>
</template>

<script>
import Button from "../common/Button.vue";

export default {
  name: "ButtonGroup",
  components: {
    Button,
  },
  props: {
    buttonStart: {
      type: Boolean,
      default: true,
    },
    buttonEnd: {
      type: Boolean,
      default: true,
    },
    align: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
    buttonLabel: {
      type: String,
      default: "Button",
    },
  },
};
</script>

<style>
.button-group {
  align-items: center;
  display: flex;
  gap: var(--size-space-400);
  position: relative;
  width: 240px;
}

.button-group .button-instance {
  display: flex !important;
  flex: 1 !important;
  flex-grow: 1 !important;
}
</style>
