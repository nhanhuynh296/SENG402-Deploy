<template>
  <v-container>
    <h1>Update your pc for FREE</h1>
    <p>First, make your terminal to be admin by sudo su</p>
    <p>Then, execute this command:</p>
    <p id="test">sudo apt update && sudo apt upgrade</p>
    <v-btn onclick="this.test()">click</v-btn>
  </v-container>

</template>

<script>
export default {
  name: "SENG406 Demo",
  data() {
  },
  methods: {
    test() {
    }
  },
  created() {
    this.test()
  }
}
</script>

<style scoped>

</style>