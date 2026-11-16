<script setup lang="ts">

import { ref, onMounted } from "vue";

import type { Image } from "./types.ts";

import ImageDash from "./dashboards/ImageDash.vue";
import axios from "axios";

const images = ref<Image[]>();

const imageMounting = async function(){

    const url = "/api/images";
    const res = await axios.get(url);
    const data = await res.data;
    images.value = res.data.images;
};

console.log("Dock and Dash.vue setting up to do image mounting....");
onMounted(imageMounting);
console.log("image mounting done...")
console.log(images);
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
            <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#image_dash">Images</button>
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
          <div class="tab-pane show active" id="image_dash"><ImageDash :images="images" /></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>