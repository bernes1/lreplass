import './index.css'
import axios from 'axios'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

axios.defaults.baseURL = import.meta.env.VITE_BASEURL || 'https://api.lreplass.no/api/v1/'

const app = createApp(App)

app.use(router)

app.mount('#app')
