<template>

<div class="d-flex">

    <AppSidebar />

    <main class="flex-grow-1 p-4 bg-light min-vh-100">

        <router-view />

    </main>

</div>

</template>

<script setup>

import AppSidebar from "./AppSidebar.vue";

</script>