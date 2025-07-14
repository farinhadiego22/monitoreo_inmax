<template>
  <div :class="['menu-item', state, className]">
    <Star8
      v-if="hasIcon"
      class="star"
      :color="state === 'hover' ? '#F5F5F5' : '#1E1E1E'"
    />
    <div class="body">
      <div class="row">
        <div class="label">{{ label }}</div>
        <MenuShortcut
          v-if="hasShortcut"
          class="menu-shortcut-instance"
          :divClassName="state === 'hover' ? 'class' : ''"
          shortcut="⇧A"
        />
      </div>
      <div v-if="hasDescription" class="div">{{ description }}</div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Star8 from "../icons/Star8.vue";
import MenuShortcut from "../layout/MenuShortcut.vue";

export default defineComponent({
  name: "MenuItem",
  components: {
    Star8,
    MenuShortcut,
  },
  props: {
    hasDescription: {
      type: Boolean,
      default: true,
    },
    hasIcon: {
      type: Boolean,
      default: true,
    },
    hasShortcut: {
      type: Boolean,
      default: true,
    },
    label: {
      type: String,
      default: "Menu Label",
    },
    description: {
      type: String,
      default: "Menu description.",
    },
    state: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
  },
});
</script>

<style>
.menu-item {
  align-items: flex-start;
  display: flex;
  gap: var(--size-space-300);
  overflow: hidden;
  padding: var(--size-space-300) var(--size-space-400) var(--size-space-300) var(--size-space-400);
  position: relative;
  width: 320px;
}

.menu-item .star {
  height: 20px !important;
  position: relative !important;
  width: 20px !important;
}

.menu-item .body {
  align-items: flex-start;
  display: flex;
  flex: 1;
  flex-direction: column;
  flex-grow: 1;
  gap: var(--size-space-100);
  position: relative;
}

.menu-item .row {
  align-items: center;
  align-self: stretch;
  display: flex;
  flex: 0 0 auto;
  justify-content: space-between;
  position: relative;
  width: 100%;
}

.menu-item .label {
  flex: 1;
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  margin-top: -1.00px;
  position: relative;
}

.menu-item .class {
  color: var(--color-text-brand-on-brand) !important;
}

.menu-item .menu-shortcut-instance {
  flex: 0 0 auto !important;
}

.menu-item .div {
  align-self: stretch;
  font-family: var(--body-small-font-family);
  font-size: var(--body-small-font-size);
  font-style: var(--body-small-font-style);
  font-weight: var(--body-small-font-weight);
  letter-spacing: var(--body-small-letter-spacing);
  line-height: var(--body-small-line-height);
  position: relative;
}

.menu-item.default {
  border-radius: var(--radius-radius-md);
}

.menu-item.hover {
  background-color: var(--color-background-brand-default);
  border-radius: var(--size-radius-200);
}

.menu-item.default .label {
  color: var(--color-text-default-default);
}

.menu-item.hover .label {
  color: var(--color-text-brand-on-brand);
}

.menu-item.default .div {
  color: var(--color-text-default-secondary);
}

.menu-item.hover .div {
  color: var(--color-text-brand-on-brand);
}
</style>
