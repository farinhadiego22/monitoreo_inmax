<script setup>
import LoginForm from './components/LoginForm.vue'
import Aperture from './components/Aperture.vue'
import madeWithInsmindRoadTrip1 from './assets/InMax.png'
</script>

<template>
  <div class="login">
    <div class="overlap-wrapper">
      <div class="overlap">
        <LoginForm class="form-log-in-instance" />

        <div class="group">
          <div class="overlap-group">
            <div class="text-wrapper-2">Web Avisadores</div>
            <Aperture class="size-48" />
          </div>
        </div>

        <img
          class="made-with-insmind"
          alt="Made with insmind"
          :src="madeWithInsmindRoadTrip1"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.login {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.overlap-wrapper {
  background-color: #ffffff;
  height: 1024px;
  overflow: hidden;
  width: 1440px;
}

.overlap {
  height: 827px;
  position: relative;
  width: 1442px;
}

.form-log-in-instance {
  display: flex;
  flex-direction: column;
  gap: 10px;
  height: 394px;
  left: 495px;
  position: absolute;
  top: 433px;
  width: 447px;
}

.form-log-in-instance input,
.form-log-in-instance button {
  padding: 12px;
  font-size: 16px;
}

.group {
  box-shadow: 0px 4px 4px #00000040;
  height: 115px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1442px;
}

.overlap-group {
  background-image: url('@/assets/rectangle-1.png');
  background-size: 100% 100%;
  height: 123px;
  position: relative;
  width: 1440px;
}

.text-wrapper-2 {
  color: #000000;
  font-family: sans-serif;
  font-size: 20px;
  left: 124px;
  position: absolute;
  top: 53px;
  width: 200px;
}

.size-48 {
  height: 45px !important;
  left: 69px !important;
  position: absolute !important;
  top: 36px !important;
  width: 47px !important;
}

.made-with-insmind {
  height: 356px;
  left: 395px;
  object-fit: cover;
  position: absolute;
  top: 50px;
  width: 356px;
}
</style>
