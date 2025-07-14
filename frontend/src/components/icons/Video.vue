<template>
  <svg
    :class="['video', className]"
    fill="none"
    height="38"
    viewBox="0 0 33 38"
    width="33"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g class="g" clip-path="url(#clip0_207_3152)">
      <path
        class="path"
        d="M31.625 11.0832L22 18.9998L31.625 26.9165V11.0832Z"
        stroke="#1E1E1E"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="4"
      />
      <path
        class="path"
        d="M19.25 7.9165H4.125C2.60622 7.9165 1.375 9.33427 1.375 11.0832V26.9165C1.375 28.6654 2.60622 30.0832 4.125 30.0832H19.25C20.7688 30.0832 22 28.6654 22 26.9165V11.0832C22 9.33427 20.7688 7.9165 19.25 7.9165Z"
        stroke="#1E1E1E"
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="4"
      />
    </g>
    <defs class="defs">
      <clipPath class="clip-path" id="clip0_207_3152">
        <rect class="rect" fill="white" height="38" width="33" />
      </clipPath>
    </defs>
  </svg>
</template>

<script>
export default {
  name: "Video",
  props: {
    className: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>
