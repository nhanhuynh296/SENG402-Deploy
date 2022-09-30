<template>
  <div>


    <v-container>
      <h1>Predictor</h1>
      <h3> {{ msg }}</h3>
      <v-card>
        <label class="form-label" for="formFileMultiple">Multiple files input example</label>
        <v-file-input id="formFileMultiple" accept="image/*" class="form-control" prepend-icon="mdi-camera" type="file"

                      @change="handleFileUpload( $event )"/>
        <v-btn :block="true" color="primary" :loading="loading" @click="onSubmit">Submit</v-btn>


      </v-card>
    </v-container>
    <h4> {{ prediction }}</h4>

    <!--      <form action = "http://localhost:5000/Upload" method = "POST"-->
    <!--            enctype = "multipart/form-data">-->
    <!--        <input type = "file" name = "file"/>-->
    <!--        <input type = "submit"/>-->
    <!--      </form>-->


  </div>

</template>

<script>
import axiosInstance from "@/router/axiosInstance";

export default {
  name: "TestComponent",
  data() {
    return {
      msg: 'Whoops, checking backend and try again!!',
      file: null,
      prediction: null,
      loading: false,
    };
  },
  methods: {
    getMessage() {
      axiosInstance.get('/')
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    onSubmit() {
      this.loading = true
      const formData = new FormData();
      formData.append('file', this.file);
      axiosInstance.post('/Predict',
          formData,
          {
            headers: {
              "content-Type": "multipart/form-data",
            },
          }).then(res => {

        console.log("PREDICTION SUCCESS!!");
        this.displayResult(res.data['result'])
      }).catch(() =>
        console.error('SEND TO BACKEND FAILURE!!')
      ).then(() => this.loading = false)
    },
    displayResult(result) {
      if (typeof result == 'object') {
        const pred = result
        const bad = pred[0]
        const good = pred[1]
        if (bad > good) {
          // this.prediction = `This image is ${100 * (1 - pred.toFixed(2))}% bad and ${100 * pred.toFixed(2)}% good.`
          this.prediction = `This image is bad, confidence: ${(100 * bad).toFixed(4)}%, good confidence:  ${(100 * good).toFixed(4)}%`
        } else if (bad < good) {
          this.prediction = `This image is good, confidence: ${(100 * good).toFixed(4)}%, , bad confidence:  ${(100 * bad).toFixed(4)}%\``
        } else {
          this.prediction = `Can not determine this image is good or bad`
        }
      } else if ((typeof result == 'number')) {
        const pred = parseFloat(result)
        if (pred > 0.5) {
          // this.prediction = `This image is ${100 * (1 - pred.toFixed(2))}% bad and ${100 * pred.toFixed(2)}% good.`
          this.prediction = `This image is good, confidence: ${(100 * pred).toFixed(4)}%`
        } else if (pred < 0.5) {
          this.prediction = `This image is bad, confidence: ${(100 * (1 - pred)).toFixed(4)}%`
        } else {
          this.prediction = `Can not determine this image is good or bad`
        }
      }
    }
  },
  created() {
    this.getMessage();
  },
};
</script>
<style scoped>

</style>