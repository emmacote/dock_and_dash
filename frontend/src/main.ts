import { createApp } from 'vue'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import DockAndDash from "./DockAndDash.vue"
const app = createApp(DockAndDash);
app.mount("#app");