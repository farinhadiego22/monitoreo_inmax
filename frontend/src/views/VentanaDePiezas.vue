<template>
  <HeaderLayout>
    <div class="ventana-de-piezas-container">
      <div class="overlap-group">
        <div class="icon-row">
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

        <div class="dates-section">
          <div>
            <input type="date" class="input-native" />
            <span class="label">Fecha de inicio</span>
          </div>
          <div>
            <input type="date" class="input-native" />
            <span class="label">Fecha de término</span>
          </div>
        </div>

        <select class="input-native select-field">
          <option value="">Selecciona campaña</option>
          <option value="A">Campaña A</option>
          <option value="B">Campaña B</option>
        </select>

        <!-- Botón flotante, dentro del overlap-group -->
        <router-link
          :to="{ name: 'CreacionDeCampana' }"
          class="fab-btn"
        >
          <span class="fab-icon">+</span>
          <span class="fab-text">Crear campaña</span>
        </router-link>
      </div>
    </div>
  </HeaderLayout>
</template>

<script>
import HeaderLayout from "@/components/layout/HeaderLayout.vue";
import Size48 from "../components/icons/Size48.vue";
import Size48_1 from "../components/icons/Size48_1.vue";

export default {
  name: "VentanaDePiezas",
  components: {
    HeaderLayout,
    Size48,
    Size48_1,
  },
};
</script>

<style scoped>
.ventana-de-piezas-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  width: 100%;
  min-height: 70vh;
  padding: 48px 0;
  background: #fff;
}

.overlap-group {
  background: url('https://c.animaapp.com/DdGYLEUA/img/rectangle-30.svg') no-repeat center/cover;
  width: 100%;
  max-width: 900px;
  min-height: 600px;
  padding: 40px 32px;
  box-shadow: 0 4px 24px #0001;
  border-radius: 28px;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

/* Botón flotante */
.fab-btn {
  position: absolute;
  bottom: 38px;
  right: 38px;
  background: linear-gradient(90deg, #2186eb, #27c2e9 90%);
  color: #fff;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.2rem;
  font-weight: 600;
  border: none;
  border-radius: 30px;
  box-shadow: 0 4px 18px #2186eb22;
  padding: 16px 28px;
  cursor: pointer;
  text-decoration: none;
  z-index: 10;
  transition: transform 0.14s, box-shadow 0.14s;
}
.fab-btn:hover {
  transform: scale(1.07);
  box-shadow: 0 6px 26px #27c2e966;
}
.fab-icon {
  font-size: 1.6rem;
  font-weight: bold;
  line-height: 1;
  margin-right: 3px;
}
.fab-text {
  font-size: 1.1rem;
  font-weight: 600;
}

.icon-row {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 20px;
}

.image {
  width: 48px;
  height: 48px;
}

.rectangle {
  width: 240px;
  height: 80px;
  object-fit: cover;
  mix-blend-mode: hard-light;
  position: absolute;
  right: 20px;
  top: 60px;
  border-radius: 18px;
}

.video-wrapper {
  width: 250px;
  height: 120px;
  background: url('https://c.animaapp.com/DdGYLEUA/img/rectangle-32.svg') no-repeat center/cover;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 24px 0;
}

.video {
  width: 48px;
  height: 48px;
}

.dates-section {
  display: flex;
  gap: 36px;
  align-items: center;
}

.input-native {
  width: 100%;
  height: 44px;
  padding: 8px 14px;
  border: 1.2px solid #b9b9b9;
  border-radius: 9px;
  font-size: 1rem;
}

.label {
  display: block;
  font-size: 1rem;
  color: #444;
  margin-top: 4px;
  font-weight: 600;
}

.select-field {
  margin-top: 20px;
  width: 320px;
}

@media (max-width: 1024px) {
  .overlap-group {
    max-width: 98vw;
    padding: 16px 4vw;
  }
}
@media (max-width: 600px) {
  .overlap-group {
    min-height: 300px;
    border-radius: 8px;
    padding: 12px 1vw;
    gap: 14px;
  }
  .rectangle {
    width: 120px;
    height: 40px;
    right: 8px;
    top: 24px;
  }
  .select-field {
    width: 100%;
  }
  .fab-btn {
    bottom: 12px;
    right: 12px;
    padding: 12px 18px;
    font-size: 1rem;
  }
  .fab-icon {
    font-size: 1.2rem;
  }
}
</style>
