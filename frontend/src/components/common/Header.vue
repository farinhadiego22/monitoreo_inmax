<template>
  <div :class="['header', className]">
    <div v-if="hasBlock" class="block">
      <div class="figma">
        <img
          class="icon"
          alt="Icon"
          src="https://c.animaapp.com/DL5zdupI/img/icon.svg"
        />
      </div>
    </div>

    <div class="navigation-pill-list">
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel"
        state="active"
      />
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel1"
        state="default"
      />
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel2"
        state="default"
      />
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel3"
        state="default"
      />
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel4"
        state="default"
        :titleClassName="navigationPillTitleClassName"
      />
      <NavigationPill
        class="navigation-pill-instance"
        :label="navigationPillLabel5"
        state="default"
        :titleClassName="navigationPillTitleClassNameOverride"
      />
    </div>

    <HeaderAuth v-if="visible" state="logged-out" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import HeaderAuth from "./HeaderAuth.vue";
import NavigationPill from "../layout/NavigationPill.vue";

export default defineComponent({
  name: "Header",
  components: {
    HeaderAuth,
    NavigationPill,
  },
  props: {
    platform: String,
    state: String,
    className: {
      type: String,
      default: "",
    },
    hasBlock: {
      type: Boolean,
      default: true,
    },
    navigationPillLabel: {
      type: String,
      default: "Pricing",
    },
    navigationPillLabel1: {
      type: String,
      default: "Solutions",
    },
    navigationPillLabel2: {
      type: String,
      default: "Community",
    },
    navigationPillLabel3: {
      type: String,
      default: "Resources",
    },
    navigationPillTitleClassName: String,
    navigationPillLabel4: {
      type: String,
      default: "Pricing",
    },
    navigationPillTitleClassNameOverride: String,
    navigationPillLabel5: {
      type: String,
      default: "Contact",
    },
    visible: {
      type: Boolean,
      default: true,
    },
  },
});
</script>

<style>
.header {
  align-items: center;
  background-color: var(--color-background-default-default);
  border-bottom-style: solid;
  border-bottom-width: 1px;
  border-color: var(--color-border-default-default);
  display: flex;
  flex-wrap: wrap;
  gap: var(--size-space-600);
  padding: var(--size-space-800);
  position: relative;
  width: var(--responsive-device-width);
}

.header .block {
  align-items: center;
  display: inline-flex;
  flex: 0 0 auto;
  gap: 24px;
  position: relative;
}

.header .figma {
  align-items: center;
  display: flex;
  justify-content: center;
  position: relative;
  width: 40px;
}

.header .icon {
  height: 38.5px;
  margin-bottom: -1.75px;
  margin-top: -1.75px;
  position: relative;
  width: 26.83px;
}

.header .navigation-pill-list {
  align-items: center;
  display: flex;
  flex: 1;
  flex-grow: 1;
  flex-wrap: wrap;
  gap: var(--size-space-200);
  justify-content: flex-end;
  position: relative;
}

.header .navigation-pill-instance {
  flex: 0 0 auto !important;
}
</style>
