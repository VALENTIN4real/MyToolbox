import { createRouter, createWebHistory } from 'vue-router'

import Ping from '@/components/Ping.vue'
import CalculatricePartageTR from '@/components/CalculatricePartageTR.vue'
import Accueil from '@/components/Accueil.vue'
import App from "@/App.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'app',
      component: Accueil
    },
    {
      path: '/calculatrice-partage-tr',
      name: 'calculatrice-partage-tr',
      component: CalculatricePartageTR
    }
  ],
})

export default router
