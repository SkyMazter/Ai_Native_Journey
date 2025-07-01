<template>
    <div class="nav">
        <h1>Momentum</h1>
        <button @click="handleAddNew"> Add New +</button>
    </div>

    <RouterView />

</template>

<style scoped>
.nav {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>

<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter()

const handleAddNew = () => router.push('/submit')
</script>