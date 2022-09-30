<template>
  <v-app>
    <v-app-bar app>
      <v-breadcrumbs
          :items="items"
          divider="-"
      ></v-breadcrumbs>
    </v-app-bar>
    <v-main>

      <router-view/>
    </v-main>
  </v-app>
</template>
<script>

import {SERVER_URL} from "@/router/axiosInstance";

export default {
  name: 'App',
  data: () => ({
    items: [
      {
        text: 'Home',
        disabled: false,
        href: '/',
      },
      {
        text: 'Prediction',
        disabled: false,
        href: '/Predict',
      },
      {
        text: 'UnLabelled',
        disabled: false,
        href: '/Labeling',
      },
      {
        text: 'Labelled',
        disabled: false,
        href: '/Labelled',
      },
    ],
  }),
  created() {
    console.log(`Using ${SERVER_URL}`)
  }
}
</script>
