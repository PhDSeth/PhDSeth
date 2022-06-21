export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'core',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],


  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    'nuxt-leaflet',
      [
        '@nuxtjs/firebase',
        {
          config: {
            apiKey: "AIzaSyDLxaaJgllch4UfzsMApfRMjX1HVtwhdyk",
            authDomain: "test-api-4e6bf.firebaseapp.com",
            databaseURL: "https://test-api-4e6bf-default-rtdb.europe-west1.firebasedatabase.app",
            projectId: "test-api-4e6bf",
            storageBucket: "test-api-4e6bf.appspot.com",
            messagingSenderId: "694645031922",
            appId: "1:694645031922:web:8d180b6ede297ea514a16b",
            measurementId: "G-HM0PPD0BSY"
          },
          services: {
            auth: {
              persistence: 'local', // default
              initialize: {
                onAuthStateChangedAction: 'onAuthStateChangedAction',
                subscribeManually: false
              },
              ssr: false, // default
            }
          }
        }
      ]
    ],

  router:{
    // middleware: ['auth'] //run before page load, this will redirect every route to login page
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
