import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router.js'
import envPlugin from '@/plugins/env.js'
import { createBootstrap } from 'bootstrap-vue-next'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

// import './assets/main.css'

const app = createApp(App);

app.use(router)
app.use(envPlugin)
app.use(createBootstrap())
app.mount('#app')
