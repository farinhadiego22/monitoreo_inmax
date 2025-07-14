<template>
  <div :class="['form-log-in', className]">
    <InputField
      class="design-component-instance-node"
      label="Email"
      state="default"
      :value="inputFieldValue"
      valueType="placeholder"
    />
    <InputField
      class="design-component-instance-node"
      label="Password"
      state="default"
      :value="inputFieldValue1"
      valueType="placeholder"
    />
    <ButtonGroup
      align="justify"
      buttonLabel="Sign In"
      buttonStart="false"
      class="button-group-instance"
      @main-click="emitLoginSuccess"
    />
    <TextLink
      class="design-component-instance-node"
      text="Forgot password?"
    />
  </div>
</template>

<script>
import InputField from "./InputField.vue";
import ButtonGroup from "../common/ButtonGroup.vue";
import TextLink from "../common/TextLink.vue";

export default {
  name: "FormLogIn",
  components: {
    InputField,
    ButtonGroup,
    TextLink,
  },
  props: {
    className: {
      type: String,
      default: "",
    },
    inputFieldValue: {
      type: String,
      default: "Ingrese su email",
    },
    inputFieldValue1: {
      type: String,
      default: "Ingrese su contraseña",
    },
  },
  methods: {
    emitLoginSuccess() {
      this.$emit('login-success');
  }
  }
};
</script>

<style>
.form-log-in {
  align-items: flex-start;
  background-color: var(--color-background-default-default);
  border: 1px solid;
  border-color: var(--color-border-default-default);
  border-radius: var(--size-radius-200);
  display: inline-flex;
  flex-direction: column;
  gap: var(--size-space-600);
  min-width: 320px;
  padding: var(--size-space-600);
  position: relative;
}

.form-log-in .design-component-instance-node {
  align-self: stretch !important;
  display: flex !important;
  flex: 0 0 auto !important;
  width: 100% !important;
}

.form-log-in .button-group-instance {
  align-self: stretch !important;
  flex: 0 0 auto !important;
  width: 100% !important;
}
</style>
