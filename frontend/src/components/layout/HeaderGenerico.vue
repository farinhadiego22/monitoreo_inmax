<template>
  <header v-if="visible" :class="['header', className]">
    <nav class="header-nav" aria-label="Main Navigation">
      <button
        v-for="(pill, i) in navigationPills"
        :key="i"
        type="button"
        :class="navigationPillTitleClassName"
        @click="$emit('navigate', pill)"
      >
        {{ pill }}
      </button>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  props: {
    className: String,
    navigationPills: {
      type: Array,
      default: () => [
        "Home", "Campaigns", "Reports", "Settings", "Profile", "Notifications"
      ]
    },
    navigationPillTitleClassName: {
      type: String,
      default: "design-component-instance-node"
    },
    visible: {
      type: Boolean,
      default: true
    }
  }
};
</script>

<style scoped>
.header {
  width: 100%;
  position: relative;
  top: 0;
  left: 0;
  background: #fff;
  z-index: 10;
  border-bottom: 1px solid #eee;
}

.design-component-instance-node {
  color: var(--color-text-positive-secondary, #222);
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  padding: 8px 12px;
  transition: background 0.2s;
}
.design-component-instance-node:hover {
  background: #f5f5f5;
}

.header-nav {
  display: flex;
  flex-direction: row;
  gap: 32px;
  align-items: center;
  padding: 16px;
}
</style>
