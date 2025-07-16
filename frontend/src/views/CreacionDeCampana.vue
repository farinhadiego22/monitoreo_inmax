<template>
  <HeaderLayout>
    <div class="main-container">
      <h2>Crear Campaña</h2>
      <div class="form-campaign">
        <InputField label="Nombre de campaña" />
        <InputField label="Descripción" />
        <InputField label="Presupuesto" />
        <InputField label="Demografía" />

        <select class="input-native">
          <option value="">Selecciona un canal</option>
          <option value="tv">TV</option>
          <option value="rrss">Redes sociales</option>
          <option value="web">Web</option>
        </select>
        <div class="form-row">
          <input type="date" class="input-native" placeholder="Fecha de inicio" />
          <input type="date" class="input-native" placeholder="Fecha de término" />
        </div>

        <AssistiveChip labelText="Subir imagen" />
        <AssistiveChip labelText="Subir video" />
        <Video />
        <Image1 />
      </div>
    </div>
  </HeaderLayout>
</template>

<script>
import HeaderLayout from "@/components/layout/HeaderLayout.vue";
import InputField from "../components/forms/InputField.vue";
import AssistiveChip from "../components/common/AssistiveChip.vue";
import Video from "../components/icons/Video.vue";
import Image1 from "../components/icons/Image1.vue";

export default {
  name: "CreacionDeCampana",
  components: {
    HeaderLayout,
    InputField,
    AssistiveChip,
    Video,
    Image1,
  },
};
</script>

<style scoped>
.main-container {
  max-width: 650px;
  margin: 0 auto;
  padding: 36px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.form-campaign {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 22px;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 32px #0001;
  padding: 36px 28px;
}
.form-row {
  display: flex;
  flex-direction: row;
  gap: 20px;
}
.input-native {
  width: 100%;
  height: 44px;
  padding: 8px 14px;
  border: 1.2px solid #b9b9b9;
  border-radius: 9px;
  margin-bottom: 10px;
  font-size: 1rem;
}
@media (max-width: 700px) {
  .form-row {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
