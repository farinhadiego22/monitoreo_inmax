<template>
  <div class="ventana-de-piezas" data-model-id="488:23996">
    <div class="overlap-group-wrapper">
      <div class="overlap-group">
        <div class="overlap">
          <Size48_1 class="image" />
        </div>

        <img
          class="rectangle"
          alt="Rectangle"
          src="https://c.animaapp.com/DdGYLEUA/img/rectangle-34.svg"
        />

        <div class="video-wrapper">
          <Size48 class="video" />
        </div>

        <DateAndTime
          class="date-and-time-compact-collapsed"
          :hasTime="false"
          month="Jun 10,"
          type="date-and-time"
          year="2024"
        />
        <div class="div">
          <DateAndTime
            class="date-and-time-compact-collapsed-instance"
            :hasTime="false"
            month="Jun 10,"
            monthClassName="date-and-time-instance"
            type="date-and-time"
            year="2024"
          />
          <div class="text-wrapper-2">Start Date</div>
        </div>

        <SelectField
          class="select-field-instance"
          label="Select campaign"
          state="default"
          value="Campaign"
          valueType="default"
        />
        <div class="text-wrapper-3">End Date</div>
      </div>
    </div>
  </div>
</template>

<script>
import Size48 from "../components/icons/Size48.vue";
import Size48_1 from "../components/icons/Size48_1.vue";
import DateAndTime from "../components/common/DateAndTime.vue";
import SelectField from "../components/common/SelectField.vue";

export default {
  name: "VentanaDePiezas",
  components: {
    Size48,
    Size48_1,
    DateAndTime,
    SelectField,
  },
};
</script>

<style>
.ventana-de-piezas {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.ventana-de-piezas .overlap-group-wrapper {
  background-color: #ffffff;
  height: 1492px;
  width: 1440px;
}

.ventana-de-piezas .overlap-group {
  background-image: url(https://c.animaapp.com/DdGYLEUA/img/rectangle-30.svg);
  background-size: 100% 100%;
  height: 750px;
  left: 310px;
  position: relative;
  top: 251px;
  width: 994px;
}

.ventana-de-piezas .overlap {
  background-image: url(https://c.animaapp.com/DdGYLEUA/img/rectangle-33.svg);
  background-size: 100% 100%;
  height: 162px;
  left: 667px;
  position: absolute;
  top: 403px;
  width: 301px;
}

.ventana-de-piezas .image {
  height: 48px !important;
  left: 121px !important;
  position: absolute !important;
  top: 43px !important;
  width: 48px !important;
}

.ventana-de-piezas .rectangle {
  height: 160px;
  left: 667px;
  mix-blend-mode: hard-light;
  position: absolute;
  top: 235px;
  width: 301px;
}

.ventana-de-piezas .video-wrapper {
  background-image: url(https://c.animaapp.com/DdGYLEUA/img/rectangle-32.svg);
  background-size: 100% 100%;
  height: 334px;
  left: 42px;
  position: absolute;
  top: 231px;
  width: 621px;
}

.ventana-de-piezas .video {
  height: 48px !important;
  left: 275px !important;
  position: absolute !important;
  top: 133px !important;
  width: 48px !important;
}

.ventana-de-piezas .date-and-time-compact-collapsed {
  left: 483px !important;
  position: absolute !important;
  top: 119px !important;
}

.ventana-de-piezas .div {
  height: 69px;
  left: 317px;
  position: absolute;
  top: 83px;
  width: 166px;
}

.ventana-de-piezas .date-and-time-instance {
  text-shadow: 0px 4px 4px #00000040 !important;
}

.ventana-de-piezas .date-and-time-compact-collapsed-instance {
  left: 0 !important;
  position: absolute !important;
  top: 35px !important;
}

.ventana-de-piezas .text-wrapper-2 {
  color: var(--color-text-default-default);
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  left: 0;
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  position: absolute;
  top: 0;
  width: 166px;
}

.ventana-de-piezas .select-field-instance {
  left: 22px !important;
  position: absolute !important;
  top: 80px !important;
}

.ventana-de-piezas .text-wrapper-3 {
  color: #000000;
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  left: 483px;
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  position: absolute;
  top: 85px;
  width: 204px;
}
</style>
