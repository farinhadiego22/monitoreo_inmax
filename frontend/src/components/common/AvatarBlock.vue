<template>
  <div :class="['avatar-block', className]">
    <Avatar
      class="avatar-instance"
      shape="circle"
      size="large"
      type="image"
    />
    <div class="info">
      <div class="text-wrapper">{{ title }}</div>
      <div class="description">{{ description }}</div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import Avatar from "./Avatar.vue";

export default defineComponent({
  name: "AvatarBlock",
  components: {
    Avatar
  },
  props: {
    title: {
      type: String,
      default: "Title",
    },
    description: {
      type: String,
      default: "Description",
    },
    className: {
      type: String,
      default: "",
    },
  },
});
</script>

<style>
.avatar-block {
  align-items: flex-start;
  display: flex;
  gap: var(--size-space-300);
  position: relative;
  width: 139px;
}

.avatar-block .avatar-instance {
  position: relative !important;
}

.avatar-block .info {
  align-items: flex-start;
  display: flex;
  flex: 1;
  flex-direction: column;
  flex-grow: 1;
  gap: 2px;
  position: relative;
}

.avatar-block .text-wrapper {
  align-self: stretch;
  color: var(--color-text-default-secondary);
  font-family: var(--body-strong-font-family);
  font-size: var(--body-strong-font-size);
  font-style: var(--body-strong-font-style);
  font-weight: var(--body-strong-font-weight);
  letter-spacing: var(--body-strong-letter-spacing);
  line-height: var(--body-strong-line-height);
  margin-top: -1.00px;
  position: relative;
}

.avatar-block .description {
  align-self: stretch;
  color: var(--color-text-default-tertiary);
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  position: relative;
}
</style>
