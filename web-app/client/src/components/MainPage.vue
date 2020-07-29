<template>
  <div>
    <h1>{{ msg }}</h1>
    <span> Analiz etmek istediğiniz mesajı veya tweet linkini giriniz </span>
    <br>
    <textarea v-model="message" placeholder="tweet url veya mesaj"></textarea>
    <br>
    <button @click="getPreds">Analyze</button>
    <br>
    <span>{{ overlayLabel }}</span>
    <br>
    <div v-if="chartsVisible">
      <BarChart
        class="chart"
        :data-set="dataOffLang"
        :colors="colorsOffLang"
        :margin-left="50"
        :margin-top="40"
        :tick-count="5"
        :bar-padding="0.5"
      />
      <BarChart
        class="chart"
        :data-set="dataCw"
        :colors="colorsCw"
        :margin-left="50"
        :margin-top="40"
        :tick-count="5"
        :bar-padding="0.5"
      />
      <BarChart
        class="chart"
        :data-set="dataSa"
        :colors="colorsSa"
        :margin-left="50"
        :margin-top="40"
        :tick-count="5"
        :bar-padding="0.5"
      />
    </div>
  </div>
</template>

<script>
import BarChart from "./BarChart.vue"
import { getPredictions } from '../predictionService'

export default {
  name: 'MainPage',
  props: {
    msg: String
  },
  data() {
    return {
      chartsVisible: false,
      message: '',
      overlayLabel: '',
      predictions: '',
      dataOffLang: null,
      dataCw: null,
      dataSa: null,
      colorsOffLang: [
        '#ffe4e4',
        '#93b5e1'
      ],
      colorsCw: [
        '#fa7d09',
        '#4a3f35'
      ],
      colorsSa: [
        '#e79cc2',
        '#e2979c',
        '#01a9b4'
      ]
    }
  },
  components: {
    BarChart
  },
  methods: {
    showOverlay() {
      this.overlayLabel= 'loading...'
    },
    hideOverlay() {
      this.overlayLabel = ''
    },
    setDataOffLang(data) {
      this.dataOffLang = [
        ['not', data.neg],
        ['offensive', data.pos]
      ]
    },
    setDataCw(data) {
      this.dataCw = [
        ['not', data.neg],
        ['checkworthy', data.pos]
      ]
    },
    setDataSa(data) {
      this.dataSa = [
        ['negative', data.neg],
        ['notr', data.notr],
        ['positive', data.pos]
      ]
    },
    async getPreds() {
      this.chartsVisible = false
      this.showOverlay()
      this.predictions = await getPredictions(this.message)
      this.hideOverlay()

      this.setDataOffLang(this.predictions.off)
      this.setDataCw(this.predictions.cw)
      this.setDataSa(this.predictions.sa)
      this.chartsVisible = true
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
