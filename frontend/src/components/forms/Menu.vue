<template>
  <div :class="['menu', className]">
    <div class="menu-header">
      <div class="text-wrapper-2">Heading</div>
      <div class="text-wrapper-3">Heading</div>
    </div>
    <MenuSeparator class="menu-separator-instance" />
    <div class="menu-section">
      <MenuItem
        class="menu-item-instance"
        description="Menu description."
        label="Menu Label"
        state="default"
      />
      <MenuItem
        class="design-component-instance-node"
        description="Menu description."
        label="Menu Label"
        state="default"
      />
      <MenuItem
        class="design-component-instance-node"
        description="Menu description."
        label="Menu Label"
        state="default"
      />
    </div>
    <MenuSeparator class="design-component-instance-node" />
    <div class="menu-section-2">
      <MenuItem
        class="design-component-instance-node"
        description="Menu description."
        label="Menu Label"
        state="default"
      />
      <MenuItem
        class="menu-item-instance"
        description="Menu description."
        label="Menu Label"
        state="default"
      />
    </div>
  </div>
</template>

<script>
import MenuItem from "./MenuItem.vue";
import MenuSeparator from "./MenuSeparator.vue";

export default {
  name: "Menu",
  components: {
    MenuItem,
    MenuSeparator
  },
  props: {
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.menu {
  align-items: flex-start;
  background-color: var(--color-background-default-default);
  border: 1px solid;
  border-color: var(--color-border-default-default);
  border-radius: var(--size-radius-200);
  box-shadow: var(--drop-shadow-300);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  padding: var(--size-space-200);
  position: relative;
  width: 301px;
}

.menu .menu-header {
  align-items: flex-start;
  align-self: stretch;
  display: flex;
  flex: 0 0 auto;
  flex-direction: column;
  padding: var(--size-space-200) var(--size-space-400) var(--size-space-100)
    var(--size-space-400);
  position: relative;
  width: 100%;
}

.menu .text-wrapper-2 {
  align-self: stretch;
  color: var(--color-text-default-secondary);
  font-family: var(--body-small-font-family);
  font-size: var(--body-small-font-size);
  font-style: var(--body-small-font-style);
  font-weight: var(--body-small-font-weight);
  letter-spacing: var(--body-small-letter-spacing);
  line-height: var(--body-small-line-height);
  margin-top: -1.00px;
  position: relative;
}

.menu .text-wrapper-3 {
  align-self: stretch;
  color: var(--color-text-default-default);
  font-family: var(--body-strong-font-family);
  font-size: var(--body-strong-font-size);
  font-style: var(--body-strong-font-style);
  font-weight: var(--body-strong-font-weight);
  letter-spacing: var(--body-strong-letter-spacing);
  line-height: var(--body-strong-line-height);
  position: relative;
}

.menu .menu-separator-instance {
  align-self: stretch !important;
  border-radius: unset !important;
  flex: 0 0 auto !important;
  padding: var(--size-space-200) var(--size-space-400) var(--size-space-200)
    var(--size-space-400) !important;
  width: 100% !important;
}

.menu .menu-section {
  align-items: flex-start;
  align-self: stretch;
  border-radius: 8px;
  display: flex;
  flex: 0 0 auto;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.menu .menu-item-instance {
  flex: 0 0 auto !important;
  width: 285px !important;
}

.menu .design-component-instance-node {
  align-self: stretch !important;
  flex: 0 0 auto !important;
  width: 100% !important;
}

.menu .menu-section-2 {
  align-items: flex-start;
  align-self: stretch;
  display: flex;
  flex: 0 0 auto;
  flex-direction: column;
  position: relative;
  width: 100%;
}
</style>
