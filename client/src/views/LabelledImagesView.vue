<template>
  <div>
    <v-container>
      <v-row justify="start">
        <v-col v-for="datum in imagesData" :key="datum.filename"
               md="4" sm="6" xl="3" xs="12">
          <LabelledImageViewerComponent :image-id="`${datum.filename}`" :label="datum.label"/>
        </v-col>
      </v-row>
    </v-container>


  </div>

</template>

<script>
import LabelledImageViewerComponent from "@/components/LabelledImageViewerComponent";
import axiosInstance from "@/router/axiosInstance";

export default {
  name: "LabelledImagesView",
  components: {LabelledImageViewerComponent},
  data() {
    return {

      pageLength: 20,
      page: 1,
      imagesData: []
    }
  },
  methods: {
    getPaginationData() {
      axiosInstance.get('labelled-images',
          {
            params: {
              page_length: this.pageLength,
              page: this.page
            }
          }).then(response => {
        console.log(response)
        this.totalPages = response.data['pages']
        this.imagesData = response.data['filenames']
      })
    },
  },
  created() {
    this.getPaginationData()
  }

}
</script>

<style scoped>

</style>