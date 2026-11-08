<script setup lang="ts">
import { ref } from "vue";
import ImageDash from "./dashboards/ImageDash.vue";
import VolumeDash from "./dashboards/VolumeDash.vue";
import ContainerDash from "./dashboards/ContainerDash.vue";
import LogDash from "./dashboards/LogDash.vue";
import NetworkDash from "./dashboards/NetworkDash.vue";
const msg = ref("Hi there.");

</script>

<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1 align="center">Dock and Dash</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-12">
        <hr />
      </div>
    </div>
    <div class="row" align="center">
      <div class="col-sm-12">

        <ul class="nav nav-tabs">
          <li class="nav-item">
            <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#images">Images</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#volumes">Volumes</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#containers">Containers</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#logs">Logs</button>
          </li>
          <li class="nav-item">
            <button class="nav-link" data-bs-toggle="tab" data-bs-target="#networks">Networks</button>
          </li>
        </ul>

      </div>
    </div>

    <div class="row">
      <div class="col-sm-12"><hr /><br /></div>
    </div>

    <div class="row">
      <div class="col-sm-12">
        <div class="tab-content">
          <div class="tab-pane show active" id="images"><ImageDash /></div>
          <div class="tab-pane" id="volumes"><VolumeDash /></div> 
          <div class="tab-pane" id="containers"><ContainerDash /></div>
          <div class="tab-pane" id="logs"><LogDash /></div>
          <div class="tab-pane" id="networks"><NetworkDash /></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>