<script setup lang="ts">

import { ref } from "vue";
import ImageDash from "./dashboards/ImageDash.vue";

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
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>