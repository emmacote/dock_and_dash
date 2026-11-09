<script setup lang="ts">
interface Image {
    id: string;
    tags: string[];
}

import {ref, onMounted }from "vue";
import axios from "axios";
const images = ref<Image[]>();

const imageMounting = async function(){

    const url = "http://localhost:5000/images";
    const res = await axios.get(url);
    const data = await res.data;
    images.value = res.data.images;
};

onMounted(imageMounting);

</script>

<template>

<h3>Images</h3>
<table class="table table-striped">
    <thead>
        <tr>
            <th>Image ID</th>
            <th>Tags</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="image in images">
            <td> {{image.id}}</td>
            <td>{{ image.tags.join(", ") }}</td>
        </tr>
    </tbody>
</table>

</template>


<style scoped land="css"></style>