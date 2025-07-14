<template>
  <div :class="['assistive-chip', state, className]">
    <div :class="['state-layer', stateLayerClassName]">
      <div class="label-text">{{ labelText }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AssistiveChip",
  props: {
    labelText: {
      type: String,
      default: "Label",
    },
    style: {
      type: Object,
      default: () => ({}),
    },
    configuration: {
      type: Object,
      default: () => ({}),
    },
    state: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
    stateLayerClassName: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.assistive-chip {
  align-items: center;
  border: 1px solid;
  border-color: var(--m3-schemes-outline);
  border-radius: 8px;
  display: inline-flex;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.assistive-chip .state-layer {
  align-items: center;
  display: inline-flex;
  flex: 0 0 auto;
  gap: 8px;
  height: 32px;
  justify-content: center;
  padding: 6px 16px;
  position: relative;
}

.assistive-chip .label-text {
  color: var(--m3-schemes-on-surface);
  font-family: var(--m3-label-large-font-family);
  font-size: var(--m3-label-large-font-size);
  font-style: var(--m3-label-large-font-style);
  font-weight: var(--m3-label-large-font-weight);
  letter-spacing: var(--m3-label-large-letter-spacing);
  line-height: var(--m3-label-large-line-height);
  margin-top: -1.00px;
  position: relative;
  text-align: center;
  white-space: nowrap;
  width: fit-content;
}

.assistive-chip.hovered {
  background-color: var(--m3-schemes-surface);
  height: 32px;
}

.assistive-chip.pressed {
  background-color: var(--m3-schemes-surface);
  height: 32px;
}

.assistive-chip.hovered .state-layer {
  background-color: #49454f14;
}

.assistive-chip.pressed .state-layer {
  background-color: #49454f1f;
}
</style>
