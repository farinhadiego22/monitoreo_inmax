<template>
  <div class="plantilla-para-el" data-model-id="489:13498">
    <div class="div-2">
      <div class="group">
        <div class="overlap-group">
          <div class="text-wrapper-5">Web Avisadores</div>
          <Aperture class="size-48-1" />
        </div>
      </div>
      <div class="overlap">
        <HeaderGenerico
          className="header-instance"
          :navigationPills="[
            'Home',
            'Campaigns',
            'Reports',
            'Settings',
            'Profile',
            'Notifications'
          ]"
          navigationPillTitleClassName="header-2"
          :visible="true"
          @navigate="onNavigate"
        />

        <AvatarBlock
          class="avatar-block-instance"
          description="Description"
          title="Title"
        />
      </div>
      <Size48 class="size-48" />
      <Menu class="menu-instance" />
    </div>
  </div>
</template>

<script>
import AvatarBlock from "../components/common/AvatarBlock.vue";
import Header from "../components/common/Header.vue";
import Menu from "../components/forms/Menu.vue";
import Aperture from "../components/icons/Aperture.vue";
import Size48 from "../components/icons/Size48.vue";
import HeaderGenerico from "../components/layout/HeaderGenerico.vue";


export default {
  name: "PlantillaParaEl",
  components: {
    AvatarBlock,
    Header,
    Menu,
    Aperture,
    Size48
  }
};
</script>

<style>
.plantilla-para-el {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.plantilla-para-el .div-2 {
  background-color: #ffffff;
  height: 1492px;
  overflow: hidden;
  position: relative;
  width: 1440px;
}

.plantilla-para-el .group {
  box-shadow: 0px 4px 4px #00000040;
  height: 115px;
  left: 0;
  position: absolute;
  top: -1px;
  width: 1442px;
}

.plantilla-para-el .overlap-group {
  background-image: url(https://c.animaapp.com/DL5zdupI/img/rectangle-1.png);
  background-size: 100% 100%;
  height: 122px;
  position: relative;
  top: 1px;
  width: 1440px;
}

.plantilla-para-el .text-wrapper-5 {
  color: #000000;
  font-family: var(--single-line-body-base-font-family);
  font-size: var(--single-line-body-base-font-size);
  font-style: var(--single-line-body-base-font-style);
  font-weight: var(--single-line-body-base-font-weight);
  left: 124px;
  letter-spacing: var(--single-line-body-base-letter-spacing);
  line-height: var(--single-line-body-base-line-height);
  position: absolute;
  top: 52px;
  width: 129px;
}

.plantilla-para-el .size-48-1 {
  height: 45px !important;
  left: 69px !important;
  position: absolute !important;
  top: 35px !important;
  width: 47px !important;
}

.plantilla-para-el .overlap {
  height: 96px;
  left: 0;
  position: absolute;
  top: 123px;
  width: 1440px;
}

.plantilla-para-el .header-instance {
  border-left-style: none !important;
  border-right-style: none !important;
  border-top-style: none !important;
  left: 0 !important;
  position: absolute !important;
  top: 0 !important;
  width: 1440px !important;
}

.plantilla-para-el .header-2 {
  color: var(--color-text-positive-secondary) !important;
}

.plantilla-para-el .avatar-block-instance {
  height: 52px !important;
  left: 8px !important;
  position: absolute !important;
  top: 6px !important;
  width: 148px !important;
}

.plantilla-para-el .size-48 {
  height: 48px !important;
  left: 7px !important;
  position: absolute !important;
  top: 219px !important;
  width: 48px !important;
}

.plantilla-para-el .menu-instance {
  height: 750px !important;
  left: 0 !important;
  position: absolute !important;
  top: 267px !important;
  width: 303px !important;
}
</style>
