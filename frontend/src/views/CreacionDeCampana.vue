<template>
  <div class="creacion-de-camapaa" data-model-id="207:3114">
    <div class="overlap-wrapper">
      <div class="overlap">
        <div class="group">
          <div class="overlap-group">
            <div class="overlap-group-wrapper">
              <div class="overlap-group-2">
                <InputField
                  class="input-field-instance"
                  :hasDiv="false"
                  inputClassName="design-component-instance-node"
                  label="Campaign Name"
                  state="default"
                  valueType="default"
                />
                <InputField
                  class="input-field-2"
                  :hasDiv="false"
                  inputClassName="input-field-3"
                  label="Campaing Description"
                  state="default"
                  valueType="default"
                />
                <InputField
                  class="input-field-4"
                  inputClassName="design-component-instance-node-2"
                  label="Budget"
                  state="default"
                  value=""
                  valueType="default"
                />
                <InputField
                  class="input-field-5"
                  :hasDiv="false"
                  inputClassName="design-component-instance-node"
                  label="Demographics"
                  state="default"
                  valueType="default"
                />
                <SelectField
                  class="select-field-instance"
                  label="Channel"
                  selectClassName="design-component-instance-node-2"
                  state="default"
                  value=""
                  valueType="default"
                />
              </div>
            </div>

            <DateAndTime
              class="date-and-time-compact-collapsed"
              month="Jun 10,"
              monthClassName="date-and-time-instance"
              time="9:41 AM"
              type="date-and-time"
              year="2024"
            />
            <div class="text-wrapper-3">Start Date</div>

            <DateAndTime
              class="date-and-time-compact-collapsed-instance"
              month="Jun 10,"
              time="9:41 AM"
              type="date-and-time"
              year="2024"
            />
            <div class="text-wrapper-4">End Date</div>
          </div>
        </div>

        <img
          class="rectangle"
          alt="Rectangle"
          src="https://c.animaapp.com/JCex60wC/img/rectangle-35.svg"
        />

        <img
          class="img"
          alt="Rectangle"
          src="https://c.animaapp.com/JCex60wC/img/rectangle-36.svg"
        />

        <AssistiveChip
          class="assistive-chip-instance"
          configuration="label-only"
          labelText="Upload image"
          state="enabled"
          stateLayerClassName="assistive-chip-2"
          style="outlined"
        />
        <Video class="video-instance" />
        <img
          class="rectangle-2"
          alt="Rectangle"
          src="https://c.animaapp.com/JCex60wC/img/rectangle-37.svg"
        />

        <Image1 class="image" />
        <AssistiveChip
          class="assistive-chip-3"
          configuration="label-only"
          labelText="Upload image"
          state="enabled"
          stateLayerClassName="assistive-chip-4"
          style="outlined"
        />
        <Image1 class="image-1" />
        <AssistiveChip
          class="assistive-chip-5"
          configuration="label-only"
          labelText="Upload video"
          state="enabled"
          stateLayerClassName="assistive-chip-6"
          style="outlined"
        />
      </div>
    </div>
  </div>
</template>

<script>
import InputField from "../components/forms/InputField.vue";
import SelectField from "../components/common/SelectField.vue";
import DateAndTime from "../components/common/DateAndTime.vue";
import AssistiveChip from "../components/common/AssistiveChip.vue";
import Video from "../components/icons/Video.vue";
import Image1 from "../components/icons/Image1.vue";

export default {
  name: "CreacionDeCamapaa",
  components: {
    InputField,
    SelectField,
    DateAndTime,
    AssistiveChip,
    Video,
    Image1,
  },
};
</script>

<style>
.creacion-de-camapaa {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.creacion-de-camapaa .overlap-wrapper {
  background-color: #ffffff;
  height: 1492px;
  width: 1440px;
}

.creacion-de-camapaa .overlap {
  height: 754px;
  left: 256px;
  position: relative;
  top: 263px;
  width: 1067px;
}

.creacion-de-camapaa .group {
  height: 754px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1067px;
}

.creacion-de-camapaa .overlap-group {
  height: 754px;
  position: relative;
  width: 1063px;
}

.creacion-de-camapaa .overlap-group-wrapper {
  height: 754px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1063px;
}

.creacion-de-camapaa .overlap-group-2 {
  background-image: url(https://c.animaapp.com/JCex60wC/img/rectangle-11.png);
  background-size: 100% 100%;
  height: 763px;
  left: -4px;
  position: relative;
  width: 1072px;
}

.creacion-de-camapaa .input-field-instance {
  display: flex !important;
  height: 72px !important;
  left: 46px !important;
  position: absolute !important;
  top: 47px !important;
  width: 981px !important;
}

.creacion-de-camapaa .design-component-instance-node {
  margin-bottom: unset !important;
  overflow: unset !important;
}

.creacion-de-camapaa .input-field-2 {
  display: flex !important;
  height: 117px !important;
  left: 46px !important;
  position: absolute !important;
  top: 136px !important;
  width: 981px !important;
}

.creacion-de-camapaa .input-field-3 {
  flex: 1 !important;
  flex-grow: 1 !important;
  overflow: unset !important;
}

.creacion-de-camapaa .input-field-4 {
  display: flex !important;
  height: 72px !important;
  left: 44px !important;
  position: absolute !important;
  top: 270px !important;
  width: 981px !important;
}

.creacion-de-camapaa .design-component-instance-node-2 {
  margin-bottom: unset !important;
}

.creacion-de-camapaa .input-field-5 {
  display: flex !important;
  height: 73px !important;
  left: 44px !important;
  position: absolute !important;
  top: 354px !important;
  width: 981px !important;
}

.creacion-de-camapaa .select-field-instance {
  display: flex !important;
  height: 78px !important;
  left: 46px !important;
  position: absolute !important;
  top: 444px !important;
  width: 337px !important;
}

.creacion-de-camapaa .date-and-time-compact-collapsed {
  left: 51px !important;
  position: absolute !important;
  top: 563px !important;
}

.creacion-de-camapaa .date-and-time-instance {
  text-shadow: 0px 4px 4px #00000040 !important;
}

.creacion-de-camapaa .text-wrapper-3 {
  color: var(--color-text-default-default);
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  left: 51px;
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  position: absolute;
  top: 531px;
  width: 166px;
}

.creacion-de-camapaa .date-and-time-compact-collapsed-instance {
  left: 51px !important;
  position: absolute !important;
  top: 656px !important;
}

.creacion-de-camapaa .text-wrapper-4 {
  color: #000000;
  font-family: var(--body-base-font-family);
  font-size: var(--body-base-font-size);
  font-style: var(--body-base-font-style);
  font-weight: var(--body-base-font-weight);
  left: 53px;
  letter-spacing: var(--body-base-letter-spacing);
  line-height: var(--body-base-line-height);
  position: absolute;
  top: 612px;
  width: 204px;
}

.creacion-de-camapaa .rectangle {
  height: 271px;
  left: 411px;
  mix-blend-mode: hard-light;
  position: absolute;
  top: 462px;
  width: 427px;
}

.creacion-de-camapaa .img {
  height: 131px;
  left: 839px;
  mix-blend-mode: hard-light;
  position: absolute;
  top: 459px;
  width: 208px;
}

.creacion-de-camapaa .assistive-chip-instance {
  display: flex !important;
  height: 26px !important;
  left: 889px !important;
  position: absolute !important;
  top: 539px !important;
  width: 107px !important;
}

.creacion-de-camapaa .assistive-chip-2 {
  margin-bottom: -3.00px !important;
  margin-left: -6.50px !important;
  margin-top: -3.00px !important;
}

.creacion-de-camapaa .video-instance {
  height: 38px !important;
  left: 608px !important;
  position: absolute !important;
  top: 558px !important;
  width: 33px !important;
}

.creacion-de-camapaa .rectangle-2 {
  height: 133px;
  left: 839px;
  mix-blend-mode: hard-light;
  position: absolute;
  top: 600px;
  width: 208px;
}

.creacion-de-camapaa .image {
  height: 39px !important;
  left: 915px !important;
  position: absolute !important;
  top: 633px !important;
  width: 43px !important;
}

.creacion-de-camapaa .assistive-chip-3 {
  display: flex !important;
  height: 26px !important;
  left: 880px !important;
  position: absolute !important;
  top: 676px !important;
  width: 109px !important;
}

.creacion-de-camapaa .assistive-chip-4 {
  margin-bottom: -3.00px !important;
  margin-left: -5.50px !important;
  margin-top: -3.00px !important;
}

.creacion-de-camapaa .image-1 {
  height: 38px !important;
  left: 914px !important;
  position: absolute !important;
  top: 494px !important;
  width: 48px !important;
}

.creacion-de-camapaa .assistive-chip-5 {
  display: flex !important;
  height: 26px !important;
  left: 568px !important;
  position: absolute !important;
  top: 612px !important;
  width: 114px !important;
}

.creacion-de-camapaa .assistive-chip-6 {
  margin-bottom: -3.00px !important;
  margin-left: -0.50px !important;
  margin-top: -3.00px !important;
}
</style>
