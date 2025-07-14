<template>
  <div class="login">
    <header class="login-header">
      <Aperture class="login-aperture" />
      <span class="login-title">Web Avisadores</span>
    </header>
    <img
      class="login-logo"
      :src="madeWithInsmind"
      alt="Logo Inmax"
    />
    <FormLogIn
      class="form-log-in-instance"
      @login-success="goToHome"
    />

  </div>
</template>

<script>
import FormLogIn from "@/components/forms/FormLogIn.vue";
import Aperture from "@/components/icons/Aperture.vue";
import madeWithInsmind from "@/assets/logoinmax.png";

export default {
  name: "Login",
  components: {
    FormLogIn,
    Aperture,
  },
  data() {
    return {
      madeWithInsmind
    };
  },
  methods: {
    goToHome() {
      this.$router.push({ name: "MenuPrincipal" });
    }
  }
};

</script>

<style>
.login {
  min-height: 100vh;
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

/* Header superior con ícono y título */
.login-header {
  display: flex;
  align-items: center;
  background: #c8f6f9;
  width: 100vw;
  height: 64px;
  padding: 0 2rem;
  box-sizing: border-box;
  box-shadow: 0 2px 8px #0001;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
}

.login-aperture {
  width: 40px;
  height: 40px;
  margin-right: 16px;
}

.login-title {
  font-weight: bold;
  font-size: 1.3rem;
  color: #222;
  letter-spacing: 1px;
}

/* Centra el logo y lo hace responsive */
.login-logo {
  width: 240px;
  max-width: 95vw;
  margin-top: 100px; /* espacio bajo el header */
  margin-bottom: 2rem;
  display: block;
}

/* El formulario */
.form-log-in-instance {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  background: #fff;
  padding: 2rem 2rem 1rem 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 24px #0001;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

/* Mejora para mobile */
@media (max-width: 600px) {
  .form-log-in-instance {
  width: 100%;
  max-width: 480px;      /* Más ancho */
  margin: 0 auto;
  background: #fff;
  padding: 2.5rem 2.5rem 2rem 2.5rem;
  border-radius: 16px;
  box-shadow: 0 2px 24px #0001;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.login-header {
  height: 56px;
  padding: 0 1rem;
  font-size: 1rem;
}
.login-logo {
  width: 320px;           /* Aumenta el tamaño */
  max-width: 98vw;
  margin-top: 120px;      /* Espacio bajo el header */
  margin-bottom: 2rem;
  display: block;
}
.login-aperture {
  width: 56px;   /* Aumenta el tamaño */
  height: 56px;
  margin-right: 24px;
}


}
</style>
