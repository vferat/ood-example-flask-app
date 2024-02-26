import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

app = createApp(App)
app.config.delimiters = ['[[', ']]'];
app.mount('#app');
