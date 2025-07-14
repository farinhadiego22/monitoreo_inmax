<template>
  <div :class="['date-and-time', className]">
    <div class="date">
      <div :class="['text-wrapper', monthClassName]">{{ month }}</div>
      <div class="text-wrapper">{{ year }}</div>
    </div>
    <div v-if="hasTime" class="time">
      <div class="text-wrapper">{{ time }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DateAndTime",
  props: {
    month: {
      type: String,
      default: "Jun 10,",
    },
    year: {
      type: String,
      default: "2024",
    },
    time: {
      type: String,
      default: "9:41 AM",
    },
    type: {
      type: String,
      default: "",
    },
    className: {
      type: String,
      default: "",
    },
    hasTime: {
      type: Boolean,
      default: true,
    },
    monthClassName: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
.date-and-time {
  align-items: center;
  border-radius: 6px;
  display: inline-flex;
  gap: 6px;
  justify-content: flex-end;
  position: relative;
}

.date-and-time .date {
  align-items: center;
  background-color: var(--system-colors-fills-tertiary);
  border-radius: 6px;
  display: inline-flex;
  flex: 0 0 auto;
  gap: 5px;
  justify-content: center;
  padding: 6px 11px;
  position: relative;
}

.date-and-time .text-wrapper {
  color: var(--system-colors-colors-blue);
  font-family: var(--body-regular-font-family);
  font-size: var(--body-regular-font-size);
  font-style: var(--body-regular-font-style);
  font-weight: var(--body-regular-font-weight);
  letter-spacing: var(--body-regular-letter-spacing);
  line-height: var(--body-regular-line-height);
  margin-top: -1.00px;
  position: relative;
  text-align: center;
  white-space: nowrap;
  width: fit-content;
}

.date-and-time .time {
  align-items: flex-start;
  background-color: var(--system-colors-fills-tertiary);
  border-radius: 6px;
  display: inline-flex;
  flex: 0 0 auto;
  gap: 10px;
  padding: 6px 11px;
  position: relative;
}
</style>
