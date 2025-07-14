<template>
  <div class="menu-principal" data-model-id="487:7541">
    <div class="div">
      <div class="group">
        <div class="overlap-group">
          <div class="text-wrapper-2">Web Avisadores</div>
          <Size48 class="aperture" />
        </div>
      </div>
      <div class="overlap">
        <img
          class="image"
          alt="Image"
          src="https://c.animaapp.com/OYuW8AoE/img/image-4@2x.png"
        />
        <div class="text-wrapper-3">Crear campaña</div>
      </div>
      <div class="overlap-2">
        <img
          class="img"
          alt="Image"
          src="https://c.animaapp.com/OYuW8AoE/img/image-6@2x.png"
        />
        <div class="text-wrapper-4">Informe financiero</div>
      </div>
      <div class="overlap-3">
        <div class="rectangle" />
        <img
          class="image-2"
          alt="Image"
          src="https://c.animaapp.com/OYuW8AoE/img/image-3@2x.png"
        />
        <div class="text-wrapper-5">Ajustes de Dashboard</div>
      </div>
      <div class="overlap-4">
        <div class="rectangle-2" />
        <img
          class="image-3"
          alt="Image"
          src="https://c.animaapp.com/OYuW8AoE/img/image-5@2x.png"
        />
        <div class="vizualizar-campa-as">
          Vizualizar campañas
          <br />
          Activas
        </div>
      </div>
      <Header
        className="header-instance"
        :hasBlock="false"
        navigationPillLabel="Home"
        navigationPillLabel1="Campaigns"
        navigationPillLabel2="Reports"
        navigationPillLabel3="Settings"
        navigationPillLabel4="Profile"
        navigationPillLabel5="Notifications"
        navigationPillTitleClassName="design-component-instance-node"
        navigationPillTitleClassNameOverride="design-component-instance-node"
        platform="desktop"
        state="default"
        :visible="false"
      />
    </div>
  </div>
</template>

<script>
import Header from "../components/common/Header.vue";
import Size48 from "../components/icons/Size48.vue";

export default {
  name: "MenuPrincipal",
  components: {
    Header,
    Size48,
  },
};
</script>

<style>
.menu-principal {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.menu-principal .div {
  background-color: #ffffff;
  height: 1024px;
  overflow: hidden;
  position: relative;
  width: 1440px;
}

.menu-principal .group {
  box-shadow: 0px 4px 4px #00000040;
  height: 115px;
  left: 0;
  position: absolute;
  top: 0;
  width: 1442px;
}

.menu-principal .overlap-group {
  background-image: url(https://c.animaapp.com/OYuW8AoE/img/rectangle-1.png);
  background-size: 100% 100%;
  height: 123px;
  position: relative;
  width: 1440px;
}

.menu-principal .text-wrapper-2 {
  color: #000000;
  font-family: var(--single-line-body-base-font-family);
  font-size: var(--single-line-body-base-font-size);
  font-style: var(--single-line-body-base-font-style);
  font-weight: var(--single-line-body-base-font-weight);
  left: 124px;
  letter-spacing: var(--single-line-body-base-letter-spacing);
  line-height: var(--single-line-body-base-line-height);
  position: absolute;
  top: 53px;
  width: 129px;
}

.menu-principal .aperture {
  height: 45px !important;
  left: 69px !important;
  position: absolute !important;
  top: 36px !important;
  width: 47px !important;
}

.menu-principal .overlap {
  background-color: #25bdbd;
  border-radius: 46px;
  box-shadow: 0px 4px 4px #00000040;
  height: 121px;
  left: 200px;
  position: absolute;
  top: 301px;
  width: 453px;
}

.menu-principal .image {
  background-blend-mode: soft-light;
  height: 110px;
  left: 172px;
  object-fit: cover;
  position: absolute;
  top: 6px;
  width: 109px;
}

.menu-principal .text-wrapper-3 {
  color: #ffffff;
  font-family: "Inter", Helvetica;
  font-size: 32px;
  font-weight: 700;
  height: 40px;
  left: 9px;
  letter-spacing: 0;
  line-height: 32px;
  position: absolute;
  text-align: center;
  top: 40px;
  width: 434px;
}

.menu-principal .overlap-2 {
  background-color: #25bdbd;
  border-radius: 46px;
  box-shadow: 0px 4px 4px #00000040;
  height: 116px;
  left: 787px;
  position: absolute;
  top: 468px;
  width: 455px;
}

.menu-principal .img {
  background-blend-mode: soft-light;
  height: 116px;
  left: 169px;
  object-fit: cover;
  position: absolute;
  top: 0;
  width: 116px;
}

.menu-principal .text-wrapper-4 {
  color: #ffffff;
  font-family: "Inter", Helvetica;
  font-size: 32px;
  font-weight: 700;
  height: 38px;
  left: 34px;
  letter-spacing: 0;
  line-height: 32px;
  position: absolute;
  text-align: center;
  top: 43px;
  white-space: nowrap;
  width: 387px;
}

.menu-principal .overlap-3 {
  height: 116px;
  left: 175px;
  position: absolute;
  top: 468px;
  width: 503px;
}

.menu-principal .rectangle {
  background-color: #48abf7;
  border-radius: 46px;
  box-shadow: 0px 4px 4px #00000040;
  height: 116px;
  left: 28px;
  position: absolute;
  top: 0;
  width: 448px;
}

.menu-principal .image-2 {
  background-blend-mode: soft-light;
  height: 81px;
  left: 212px;
  object-fit: cover;
  position: absolute;
  top: 23px;
  width: 81px;
}

.menu-principal .text-wrapper-5 {
  color: #ffffff;
  font-family: "Inter", Helvetica;
  font-size: 32px;
  font-weight: 700;
  height: 38px;
  left: 0;
  letter-spacing: 0;
  line-height: 32px;
  position: absolute;
  text-align: center;
  top: 43px;
  white-space: nowrap;
  width: 503px;
}

.menu-principal .overlap-4 {
  height: 121px;
  left: 743px;
  position: absolute;
  top: 301px;
  width: 521px;
}

.menu-principal .rectangle-2 {
  background-color: #48abf7;
  border-radius: 46px;
  box-shadow: 0px 4px 4px #00000040;
  height: 121px;
  left: 39px;
  position: absolute;
  top: 0;
  width: 457px;
}

.menu-principal .image-3 {
  background-blend-mode: soft-light;
  height: 98px;
  left: 222px;
  object-fit: cover;
  position: absolute;
  top: 12px;
  width: 98px;
}

.menu-principal .vizualizar-campa-as {
  color: #ffffff;
  font-family: "Inter", Helvetica;
  font-size: 32px;
  font-weight: 700;
  height: 93px;
  left: 0;
  letter-spacing: 0;
  line-height: 32px;
  position: absolute;
  text-align: center;
  top: 18px;
  width: 521px;
}

.menu-principal .header-instance {
  border-left-style: none !important;
  border-right-style: none !important;
  border-top-style: none !important;
  left: -3px !important;
  position: absolute !important;
  top: 115px !important;
  width: 1440px !important;
}

.menu-principal .design-component-instance-node {
  color: var(--color-text-positive-secondary) !important;
}
</style>
