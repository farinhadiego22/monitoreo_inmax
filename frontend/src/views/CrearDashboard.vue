<template>
  <HeaderLayout>
    <div class="main-container">
      <h2>Playground de Dashboard (Demo)</h2>
      <div class="dashboard-settings-container">
        <div class="selectors">
          <div class="field">
            <label>Selecciona datos:</label>
            <select v-model="selectedDataset" class="input-native">
              <option value="" disabled>Elige un set de datos</option>
              <option v-for="d in datasets" :key="d.key" :value="d.key">{{ d.label }}</option>
            </select>
          </div>
          <div class="field">
            <label>Tipo de gráfico:</label>
            <select v-model="selectedChart" class="input-native">
              <option value="" disabled>Elige un gráfico</option>
              <option value="bar">Barras</option>
              <option value="pie">Torta</option>
              <option value="line">Tendencia</option>
            </select>
          </div>
        </div>
        <div class="chart-preview">
          <div v-if="selectedDataset && selectedChart" class="fake-chart">
            <img
              v-if="selectedChart === 'bar'"
              src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
              alt="Bar Chart"
              class="chart-img"
            />
            <img
              v-else-if="selectedChart === 'pie'"
              src="https://cdn-icons-png.flaticon.com/512/3135/3135714.png"
              alt="Pie Chart"
              class="chart-img"
            />
            <img
              v-else-if="selectedChart === 'line'"
              src="https://cdn-icons-png.flaticon.com/512/3135/3135718.png"
              alt="Line Chart"
              class="chart-img"
            />
            <div class="chart-caption">
              Mostrando gráfico tipo <b>{{ chartTypeLabel }}</b> para <b>{{ datasetLabel }}</b>.
            </div>
          </div>
          <div v-else class="empty-chart-msg">Selecciona datos y gráfico para previsualizar.</div>
        </div>
      </div>
    </div>
  </HeaderLayout>
</template>

<script>
import HeaderLayout from "@/components/layout/HeaderLayout.vue";

export default {
  name: "CrearDashboard",
  components: { HeaderLayout },
  data() {
    return {
      selectedDataset: "",
      selectedChart: "",
      datasets: [
        { key: "demografia", label: "Datos demográficos" },
        { key: "rendimiento", label: "Rendimiento campañas" },
        { key: "sexo", label: "Distribución por sexo" }
      ]
    }
  },
  computed: {
    datasetLabel() {
      const found = this.datasets.find(d => d.key === this.selectedDataset);
      return found ? found.label : '';
    },
    chartTypeLabel() {
      switch (this.selectedChart) {
        case 'bar': return 'Barras'
        case 'pie': return 'Torta'
        case 'line': return 'Tendencia'
        default: return ''
      }
    }
  }
};
</script>

<style scoped>
.main-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 36px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
h2 {
  margin-bottom: 28px;
  color: #222;
  font-weight: 700;
  letter-spacing: 0.5px;
}
.dashboard-settings-container {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 32px #0001;
  width: 100%;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 28px;
  align-items: center;
}
.selectors {
  display: flex;
  gap: 40px;
  width: 100%;
  justify-content: center;
}
.field {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 180px;
}
.input-native {
  width: 100%;
  height: 44px;
  padding: 8px 14px;
  border: 1.2px solid #b9b9b9;
  border-radius: 9px;
  font-size: 1rem;
  margin-bottom: 6px;
}
.chart-preview {
  width: 100%;
  min-height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.fake-chart {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.chart-img {
  width: 120px;
  margin-bottom: 18px;
  opacity: 0.92;
}
.chart-caption {
  font-size: 1.15rem;
  color: #222;
  text-align: center;
}
.empty-chart-msg {
  color: #aaa;
  font-size: 1.15rem;
  font-style: italic;
  text-align: center;
}
@media (max-width: 700px) {
  .dashboard-settings-container {
    padding: 10px;
  }
  .selectors {
    flex-direction: column;
    gap: 16px;
    width: 100%;
    align-items: stretch;
  }
}
</style>
