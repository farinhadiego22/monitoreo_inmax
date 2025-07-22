<template>
  <div>
    <canvas ref="canvas"></canvas>
  </div>
</template>
<script setup>
import { ref, watch, onMounted } from "vue";
import { Chart, BarController, BarElement, CategoryScale, LinearScale } from "chart.js";
Chart.register(BarController, BarElement, CategoryScale, LinearScale);

const props = defineProps({
  labels: Array,
  values: Array,
});

const canvas = ref(null);
let chart = null;

const renderChart = () => {
  if (chart) chart.destroy();
  chart = new Chart(canvas.value, {
    type: "bar",
    data: {
      labels: props.labels,
      datasets: [{
        label: "Interacciones por edad",
        data: props.values,
        backgroundColor: "#26b2d5"
      }]
    }
  });
};
onMounted(renderChart);
watch([() => props.labels, () => props.values], renderChart);
</script>
