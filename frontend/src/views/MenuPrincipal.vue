<template>
  <HeaderLayout>
    <div class="main-container">
      <div class="menu-content">
        <!-- Botón Crear campaña -->
        <router-link to="/creacion-de-campana" class="menu-btn teal">
          <img
            class="menu-img"
            alt="Image"
            src="https://c.animaapp.com/OYuW8AoE/img/image-4@2x.png"
          />
          <span>Crear campaña</span>
        </router-link>

        <router-link
          :to="{ name: 'InformeFinanciero' }"
            class="menu-btn teal"
        >
          <img
            class="menu-img"
            alt="Image"
            src="https://c.animaapp.com/OYuW8AoE/img/image-6@2x.png"
          />
          <span>Informe financiero</span>
        </router-link>

        <router-link
          :to="{ name: 'CrearDashboard' }"
          class="menu-btn blue"
        >
          <img
            class="menu-img"
            alt="Image"
            src="https://c.animaapp.com/OYuW8AoE/img/image-3@2x.png"
          />
          <span>Ajustes de Dashboard</span>
        </router-link>


        <!-- Botón Visualizar campañas activas -->
        <router-link to="/ventana-de-piezas" class="menu-btn blue">
          <img
            class="menu-img"
            alt="Image"
            src="https://c.animaapp.com/OYuW8AoE/img/image-5@2x.png"
          />
          <span>
            Vizualizar campañas
          </span>
        </router-link>
      </div>
    </div>
  </HeaderLayout>
</template>

<script>
import HeaderLayout from "@/components/layout/HeaderLayout.vue";
export default {
  name: "MenuPrincipal",
  components: { HeaderLayout },
};
</script>

<style scoped>
.main-container {
  width: 100%;
  max-width: 1300px; /* Ajusta a tu gusto */
  margin: 0 auto;
  padding: 0 24px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.menu-content {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px 60px;
  padding: 80px 0;
}

.menu-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 420px;
  height: 120px;
  border-radius: 46px;
  box-shadow: 0 4px 4px #00000040;
  color: #fff;
  font-size: 2.2rem;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
  text-decoration: none;
  transition: transform .08s;
  background: #25bdbd;
}

.menu-btn.blue {
  background: #48abf7;
}
.menu-btn.teal {
  background: #25bdbd;
}
.menu-btn:hover {
  transform: scale(1.03);
}
.menu-img {
  width: 72px;
  height: 72px;
  object-fit: contain;
  margin-bottom: 10px;
}

/* Responsive para móvil */
@media (max-width: 900px) {
  .main-container {
    max-width: 100vw;
    padding: 0 8px;
  }
  .menu-btn {
    width: 95vw;
    min-width: 220px;
    max-width: 400px;
  }
  .menu-content {
    gap: 22px 12px;
    padding: 36px 0;
  }
}
</style>
