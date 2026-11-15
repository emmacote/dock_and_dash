<script setup lang="ts">

import type { Image } from "../types.ts";
import {ref } from "vue";

const props = defineProps<{
    images: Image[]
}>();

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