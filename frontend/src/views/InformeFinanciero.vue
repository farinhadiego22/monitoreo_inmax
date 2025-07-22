<template>
  <HeaderLayout>
    <div class="main-container">
      <h2>Informe financiero</h2>
      <div class="campaigns-financial-list">
        <div
          v-for="(campaign, idx) in campaigns"
          :key="idx"
          class="campaign-card"
          @click="verDetalle(campaign)"
          style="cursor:pointer"
        >
          <div class="card-header">
            <span class="card-title">{{ campaign.name }}</span>
            <span class="card-status" :class="campaign.statusClass">{{ campaign.status }}</span>
          </div>
          <div class="card-kpis">
            <div class="kpi">
              <span class="kpi-label">Presupuesto</span>
              <span class="kpi-value">${{ campaign.budget.toLocaleString() }}</span>
            </div>
            <div class="kpi">
              <span class="kpi-label">Impresiones</span>
              <span class="kpi-value">{{ campaign.impressions.toLocaleString() }}</span>
            </div>
            <div class="kpi">
              <span class="kpi-label">Clics</span>
              <span class="kpi-value">{{ campaign.clicks.toLocaleString() }}</span>
            </div>
            <div class="kpi">
              <span class="kpi-label">CTR</span>
              <span class="kpi-value">{{ campaign.ctr }}%</span>
            </div>
            <div class="kpi">
              <span class="kpi-label">CPC</span>
              <span class="kpi-value">${{ campaign.cpc }}</span>
            </div>
          </div>
          <div class="card-dates">
            <span>Inicio: <strong>{{ campaign.start }}</strong></span>
            <span>Fin: <strong>{{ campaign.end }}</strong></span>
          </div>
        </div>
      </div>
    </div>
  </HeaderLayout>
</template>

<script>
import HeaderLayout from "@/components/layout/HeaderLayout.vue";

export default {
  name: "InformeFinanciero",
  components: { HeaderLayout },
  data() {
    return {
      campaigns: [
        {
          slug: "campana-invierno",              // <--- Agregado
          name: "Campaña Invierno",
          status: "Activa",
          statusClass: "status-activa",
          budget: 5000,
          impressions: 120000,
          clicks: 3200,
          ctr: 2.7,
          cpc: 1.56,
          start: "01/07/24",
          end: "07/08/24"
        },
        {
          slug: "verano-2024",                   // <--- Agregado
          name: "Verano 2024",
          status: "Activa",
          statusClass: "status-activa",
          budget: 6500,
          impressions: 145000,
          clicks: 4100,
          ctr: 2.8,
          cpc: 1.42,
          start: "12/12/23",
          end: "29/02/24"
        },
        {
          slug: "lanzamiento-web",               // <--- Agregado
          name: "Lanzamiento Web",
          status: "Activa",
          statusClass: "status-activa",
          budget: 8000,
          impressions: 175500,
          clicks: 5900,
          ctr: 3.4,
          cpc: 1.36,
          start: "10/06/24",
          end: "30/08/24"
        }
      ]
    };
  },

  methods: {
    verDetalle(campaign) {
      this.$router.push({
        name: "DetalleCampaña",
        params: { slug: campaign.slug }    // <--- AHORA USAS slug
      });
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

.campaigns-financial-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.campaign-card {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 4px 32px #0001;
  padding: 28px 36px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.35rem;
}
.card-title {
  font-weight: 600;
  color: #26b2d5;
}
.card-status {
  font-size: 1rem;
  font-weight: 700;
  padding: 4px 18px;
  border-radius: 12px;
  background: #e7fcf8;
  color: #22ad76;
  letter-spacing: 0.5px;
}
.status-activa {
  background: #e7fcf8;
  color: #22ad76;
}
.card-kpis {
  display: flex;
  flex-wrap: wrap;
  gap: 36px 60px;
  margin-bottom: 8px;
}
.kpi {
  display: flex;
  flex-direction: column;
  min-width: 120px;
}
.kpi-label {
  color: #888;
  font-size: 0.95rem;
}
.kpi-value {
  font-size: 1.15rem;
  font-weight: 600;
  color: #222;
  margin-top: 2px;
}
.card-dates {
  display: flex;
  gap: 26px;
  font-size: 1rem;
  color: #606060;
}

@media (max-width: 700px) {
  .main-container {
    padding: 18px 3vw;
  }
  .campaign-card {
    padding: 14px 10px;
  }
  .card-kpis {
    gap: 18px 10px;
  }
}
</style>
