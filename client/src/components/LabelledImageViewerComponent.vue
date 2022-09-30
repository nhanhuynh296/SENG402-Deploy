<template>
  <v-card elevation="7" min-width="16rem">
    <v-img :src="imageURL" height="250"/>

    <v-card-text>
      <v-btn-toggle v-model="newLabel" class="button-group" mandatory @click="change">
        <v-btn color="red" value="Bad">Bad</v-btn>
        <v-btn color="yellow" value="Marginal">Marginal</v-btn>
        <v-btn color="green" value="Good">Good</v-btn>
      </v-btn-toggle>
    </v-card-text>

  </v-card>
</template>

<script>
import AxiosInstance, {SERVER_URL} from "@/router/axiosInstance";

export default {
  name: "LabelledImageViewerComponent",
  props: {
    imageId: String,
    label: Number
  },
  data() {
    return {
      imageURL: `${SERVER_URL}/images/${this.imageId}`,
      labelMapper: {"1": "Good", "-1": "Bad", "0": "Marginal"},
      newLabel: String,
      loading: false,

    }
  },
  methods: {
    change() {
      console.log(this.newLabel)
      this.loading = true
      AxiosInstance.put(`/images/${this.imageId}`,
          {
            label: this.newLabel
          }).then(() => {
        this.loading = false
      })
    }
  },
  created() {
    this.newLabel = this.labelMapper[this.label]
  }


}
</script>

<style scoped>
.button-group > * {
  flex: 1 1 0;
}
</style>