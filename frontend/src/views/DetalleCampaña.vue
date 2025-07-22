<template>
  <HeaderLayout>
    <div class="main-container">
      <button @click="$router.back()" class="volver-btn">← Volver</button>
      <h2>Detalle de campaña: {{ nombreCampaña }}</h2>
      <div v-if="loading">Cargando informe...</div>
      <div v-else>
        <div class="kpis">
          <div>Total interacciones: <b>{{ kpis?.total_interacciones }}</b></div>
          <div>Total bonos: <b>${{ kpis?.total_bonos }}</b></div>
          <div>Presupuesto restante: <b>${{ kpis?.presupuesto_restante }}</b></div>
        </div>
        <!-- Gráfico de ejemplo (por edad) -->
        <BarChart v-if="kpis" :labels="labelsEdad" :values="valuesEdad" />
      </div>
    </div>
  </HeaderLayout>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { useRoute } from "vue-router"
import HeaderLayout from "@/components/layout/HeaderLayout.vue"
import BarChart from "@/components/common/BarChart.vue"

const route = useRoute()
const slug = route.params.slug

const loading = ref(true)
const kpis = ref(null)
const nombreCampaña = ref('')

// Datos mock para distintas campañas
const campañasMock = [
  {
    slug: "campana-invierno",
    nombre: "Campaña Invierno",
    kpis: {
      total_interacciones: 142,
      total_bonos: 71,
      presupuesto_restante: 4929,
      interacciones_por_edad: { "24": 45, "26": 36, "27": 61 }
    }
  },
  {
    slug: "verano-2024",
    nombre: "Verano 2024",
    kpis: {
      total_interacciones: 189,
      total_bonos: 80,
      presupuesto_restante: 6311,
      interacciones_por_edad: { "24": 65, "26": 54, "27": 70 }
    }
  },
  {
    slug: "lanzamiento-web",
    nombre: "Lanzamiento Web",
    kpis: {
      total_interacciones: 220,
      total_bonos: 90,
      presupuesto_restante: 7900,
      interacciones_por_edad: { "24": 80, "26": 70, "27": 70 }
    }
  }
]

onMounted(() => {
  // Busca la campaña por slug
  const camp = campañasMock.find(c => c.slug === slug)
  if (camp) {
    nombreCampaña.value = camp.nombre
    kpis.value = camp.kpis
  } else {
    nombreCampaña.value = "No encontrada"
    kpis.value = null
  }
  loading.value = false
})

const labelsEdad = computed(() => kpis.value ? Object.keys(kpis.value.interacciones_por_edad) : [])
const valuesEdad = computed(() => kpis.value ? Object.values(kpis.value.interacciones_por_edad) : [])
</script>

<style scoped>
.main-container {
  max-width: 700px;
  margin: 0 auto;
  padding: 34px 20px;
}
h2 {
  margin-bottom: 22px;
}
.kpis {
  display: flex;
  gap: 24px;
  margin-bottom: 30px;
}
.volver-btn {
  background: #eee;
  border: none;
  border-radius: 8px;
  padding: 7px 20px;
  margin-bottom: 14px;
  cursor: pointer;
  font-size: 1.03rem;
  color: #2097b8;
  transition: background 0.2s;
}
.volver-btn:hover {
  background: #d3f4fc;
}
</style>
