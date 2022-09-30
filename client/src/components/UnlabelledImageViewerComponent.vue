<template>

  <v-card elevation="7" min-width="16rem">


    <v-img :src="imageURL" max-height="17rem" min-height="17rem"
           v-on:click="popupModal=true"/>


    <v-dialog v-model="popupModal" :fullscreen="true" :scrim="false" transition="dialog-bottom-transition">

      <v-card>

        <v-img :src="imageURL">
          <v-btn :icon="true" @click="popupModal = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-img>
      </v-card>

    </v-dialog>


    <v-card-text>
      <v-btn-toggle v-model="label" :disabled="done" mandatory style="width: 100%">
        <v-btn color="red" style="width: 33%" value="Bad">Bad</v-btn>
        <v-btn color="yellow" style="width: 33%" value="Marginal">Marginal</v-btn>
        <v-btn color="green" style="width: 33%" value="Good">Good</v-btn>
      </v-btn-toggle>
    </v-card-text>

    <v-card-text>
      <v-btn v-if="!done" :block="true" :disabled="label===null" :loading="loading" color="primary"
             @click="onSubmit">Submit
      </v-btn>
    </v-card-text>
  </v-card>


</template>

<script>
import axiosInstance, {SERVER_URL} from "@/router/axiosInstance";

export default {
  name: "ImageLabelingComponent",
  props: {
    imageId: String
  },
  data() {
    return {
      imageURL: `${SERVER_URL}/images/${this.imageId}`,
      label: null,
      loading: false,
      done: false,
      popupModal: false,
    }
  },
  methods: {
    onSubmit() {
      this.loading = true
      axiosInstance.put(`/images/${this.imageId}`,
          {
            label: this.label
          }).then(() => {
        this.done = true

      })
    }
  }
}
</script>

<style scoped>

</style>