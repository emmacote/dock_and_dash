<script setup lang="ts">

import type { Image } from "../types.ts";

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
            <th>Created</th>
            <th>OS</th>
            <th>Architecture</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="image in images">
            <td> {{ image.Id }}</td>
            <td>{{ image.Created }}</td>
            <td>{{  image.Os }}</td>
            <td>{{  image.Architecture }}</td>
            <td>{{  image.Comment }}</td>
        </tr>
    </tbody>
</table>

</template>


<style scoped land="css"></style>