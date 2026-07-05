<template>
    <div class="input-group search-wrapper">
        <span class="input-group-text bg-transparent border-0 ps-3 pe-2 search-icon">
            <i class="bi bi-search"></i>
        </span>
        <input
            v-model="store.search"
            class="form-control bg-transparent border-0 shadow-none py-2 search-input"
            placeholder="Search task..."
        >
    </div>
</template>

<script setup>
import { useTaskStore } from "@/stores/taskStore"

const store = useTaskStore()
</script>

<style scoped>
.search-wrapper {
    background-color: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #e9ecef;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.search-wrapper:focus-within {
    background-color: #ffffff;
    border-color: #4361ee;
    box-shadow: 0 0 0 4px rgba(67, 97, 238, 0.15);
    transform: translateY(-1px);
}

.search-wrapper:focus-within .search-icon {
    color: #4361ee !important;
}

.search-icon {
    color: #adb5bd;
    transition: color 0.3s ease;
}

.search-input {
    font-size: 0.95rem;
}

.search-input::placeholder {
    color: #adb5bd;
    transition: color 0.3s ease;
}

.search-wrapper:focus-within .search-input::placeholder {
    color: #ced4da;
}
</style>