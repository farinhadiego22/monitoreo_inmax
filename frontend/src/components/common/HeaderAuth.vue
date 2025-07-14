<template>
  <div class="header-auth">
    <Button
      class="button-instance"
      label="Sign in"
      size="small"
      state="default"
      variant="neutral"
    />
    <Button
      class="button-instance"
      label="Register"
      size="small"
      state="default"
      variant="primary"
    />
  </div>
</template>

<script>
import Button from "./Button.vue";

export default {
  name: "HeaderAuth",
  components: {
    Button
  },
  props: {
    state: {
      type: String,
      default: ""
    }
  }
};
</script>

<style>
.header-auth {
  align-items: center;
  display: flex;
  gap: var(--size-space-300);
  position: relative;
  width: 178px;
}

.header-auth .button-instance {
  display: flex !important;
  flex: 1 !important;
  flex-grow: 1 !important;
}
</style>
