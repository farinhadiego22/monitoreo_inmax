<template>
  <div class="header-layout">
    <header class="header-bar">
      <div class="header-container">
        <div class="header-left">
          <img
            src="https://c.animaapp.com/DL5zdupI/img/icon.svg"
            class="logo-figma"
            alt="Logo"
          />
          <span class="title">Web Avisadores</span>
        </div>
        <div class="header-right">
          <nav class="nav-header">
            <router-link to="/menu-principal">{{ navigationPillLabel }}</router-link>
            <router-link to="/ventana-de-piezas">{{ navigationPillLabel1 }}</router-link>
            <router-link to="/informe-financiero">{{ navigationPillLabel2 }}</router-link>
            <router-link to="/crear-dashboard">{{ navigationPillLabel3 }}</router-link>
            <router-link to="/perfil">{{ navigationPillLabel4 }}</router-link>
            <router-link to="/notificaciones">{{ navigationPillLabel5 }}</router-link>
          </nav>
        </div>
      </div>
    </header>
    <main class="header-layout-main">
      <slot />
    </main>
  </div>
</template>

<script>
export default {
  name: 'HeaderLayout',
  props: {
    navigationPillLabel: { type: String, default: 'Home' },
    navigationPillLabel1: { type: String, default: 'Campaigns' },
    navigationPillLabel2: { type: String, default: 'Reports' },
    navigationPillLabel3: { type: String, default: 'Settings' },
    navigationPillLabel4: { type: String, default: 'Profile' },
    navigationPillLabel5: { type: String, default: 'Notifications' },
  }
}
</script>

<style scoped>
.header-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  min-height: 90px;
  background: #a9f2f2;
  box-shadow: 0px 4px 4px #00000040;
  z-index: 1000;
  display: flex;
  justify-content: center;
}
.header-container {
  width: 100%;
  max-width: 1380px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 36px;
}
.header-left {
  display: flex;
  align-items: center;
}
.logo-figma {
  height: 38px;
  margin-right: 14px;
  vertical-align: middle;
}
.title {
  font-size: 1.6rem;
  font-weight: bold;
  color: #fff;
}
.header-right {
  display: flex;
  align-items: center;
}

/* --- Botones de navegación --- */
.nav-header {
  display: flex;
  flex-direction: row;
  gap: 28px;
  align-items: center;
}
.nav-header a {
  color: #1986ac;
  font-weight: 500;
  text-decoration: none;
  padding: 7px 18px;
  border-radius: 6px;
  transition: background 0.13s, color 0.13s;
  font-size: 1.1rem;
  background: none;
}
.nav-header a.router-link-exact-active,
.nav-header a.router-link-active {
  background: #ecfcfc;
  color: #015367;
  font-weight: bold;
}
.nav-header a:hover {
  background: #b4eafd;
  color: #0179b8;
}

.header-layout-main {
  width: 100vw;
  margin-top: 90px;
  padding: 32px 10vw 32px 10vw;
  box-sizing: border-box;
  min-height: calc(100vh - 90px);
  display: flex;
  flex-direction: column;
  align-items: center;
}
@media (max-width: 900px) {
  .header-container {
    max-width: 100vw;
    padding: 0 12px;
  }
  .header-bar {
    min-height: 64px;
  }
  .header-layout-main {
    padding: 24px 4vw 24px 4vw;
    margin-top: 72px;
  }
  .nav-header {
    gap: 10px;
  }
}
@media (max-width: 600px) {
  .logo-figma {
    height: 28px;
    margin-right: 8px;
  }
  .title {
    font-size: 1.2rem;
  }
  .header-layout-main {
    padding: 12px 2vw;
    margin-top: 60px;
  }
}
</style>
