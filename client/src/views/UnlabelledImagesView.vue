<template>
  <v-container>
    <h1>Labeling Images</h1>

    <label class="form-label" for="formFileMultiple">Multiple files input example</label>
    <v-file-input id="formFileMultiple" :multiple="true" accept="image/*" class="form-control" prepend-icon="mdi-camera"
                  type="file" @change="handleFileUpload( $event )"/>
    <v-btn :block="true" color="primary" @click="onSubmit">Submit</v-btn>

    <v-container>
      <v-row justify="start">
        <v-col v-for="filename in imagesFilename" :key="filename"
               md="4" sm="6" xl="3" xs="12">
          <ImageLabelingComponent :image-id="`${filename}`"/>
        </v-col>
      </v-row>
    </v-container>

  </v-container>
</template>

<script>
import ImageLabelingComponent from "@/components/UnlabelledImageViewerComponent";
import axiosInstance from "@/router/axiosInstance";

export default {
  name: "LabelingComponent",
  components: {ImageLabelingComponent},
  data() {
    return {
      totalPages: 0,
      page: 1,
      pageLength: 20,
      imagesFilename: []
    }
  },
  methods: {
    getPaginationData() {
      axiosInstance.get('unlabelled-images',
          {
            params: {
              page_length: this.pageLength,
              page: this.page
            }
          }).then(response => {
        this.totalPages = response.data.pages
        this.imagesFilename = response.data['filenames']
      })
    },
    handleFileUpload(event) {
      this.file = event.target.files;
    },
    onSubmit() {
      const formData = new FormData();
      for (let i = 0; i < this.file.length; i++) {
        formData.append('file', this.file[i]);
        console.log(this.file[i])
      }
      // formData.append('file', this.file);
      axiosInstance.post('/unlabelled-images',
          formData,
          {
            headers: {
              "content-Type": "multipart/form-data",
            },
          })
    }
  },
  created() {
    this.getPaginationData()
  }
}
</script>

<style scoped>

</style>