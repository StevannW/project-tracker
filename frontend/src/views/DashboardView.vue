<template>
<div class="container pb-4 pt-0">

<div class="d-flex flex-column flex-md-row justify-content-between align-items-start align-items-md-center mb-4 gap-3">
    <div class="animate-fade-in">
        <h2 class="fw-bold mb-1"><span class="text-gradient">Dashboard</span></h2>
        <p class="text-muted mb-0">
            Manage your daily tasks now
        </p>
    </div>
    <div class="d-flex align-items-center px-3 px-md-4 py-2 rounded-pill animate-fade-in clock-pill justify-content-center justify-content-md-start" style="background: linear-gradient(145deg, #ffffff, #f8f9fa); box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid rgba(233, 236, 239, 0.5); animation-delay: 0.1s;">
        <i class="bi bi-clock text-primary me-2 me-md-3 d-none d-md-inline-block" style="font-size: 1rem; filter: drop-shadow(0 2px 3px rgba(67, 97, 238, 0.3));"></i>
        <span class="fw-bold d-none d-md-inline" style="color: #495057; font-size: 0.95rem; letter-spacing: 0.3px;">{{ currentDateTime }}</span>
        
        <span class="fw-bold d-md-none" style="color: #495057; font-size: 0.85rem; letter-spacing: 0.3px;">{{ shortDateOnly }}</span>
        <i class="bi bi-clock text-primary mx-2 d-md-none" style="font-size: 0.9rem; filter: drop-shadow(0 2px 3px rgba(67, 97, 238, 0.3));"></i>
        <span class="fw-bold d-md-none" style="color: #495057; font-size: 0.85rem; letter-spacing: 0.3px;">{{ shortTimeOnly }}</span>
    </div>
</div>

<SummaryCards/>

<div class="d-flex flex-wrap justify-content-between align-items-center mb-4 gap-3 animate-fade-in" style="animation-delay: 0.2s; position: relative; z-index: 10;">
    <div style="width: 480px; max-width: 100%;">
        <SearchBar/>
    </div>
    
    <div class="d-flex align-items-center gap-2">
        <div class="dropdown position-relative" ref="sortDropdownRef">
            <button 
                class="btn bg-white border d-flex align-items-center shadow-sm hover-lift" 
                type="button" 
                @click="toggleSort"
                style="border-radius: 8px; height: 40px; padding: 0 16px; transition: all 0.2s;"
            >
                <i class="bi" :class="taskStore.sortOrder === 'desc' ? 'bi-sort-down' : 'bi-sort-up'" style="font-size: 0.9rem; color: #6c757d; margin-right: 8px;"></i>
                <span class="fw-medium text-dark" style="font-size: 0.85rem;">
                    {{ taskStore.sortOrder === 'desc' ? 'Latest' : 'Oldest' }}
                </span>
                <i class="bi bi-chevron-down ms-2 text-muted" style="font-size: 0.75rem;"></i>
            </button>
            <ul class="dropdown-menu dropdown-menu-end shadow border-0 mt-2" :class="{ show: isSortOpen }" style="position: absolute; right: 0; top: 100%; border-radius: 12px; padding: 8px; min-width: 140px; font-size: 0.85rem; z-index: 1000;">
                <li>
                    <a class="dropdown-item rounded fw-medium mb-1 d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.sortOrder === 'desc'}" 
                       href="#" @click.prevent="setSort('desc')">
                       Latest
                       <i v-if="taskStore.sortOrder === 'desc'" class="bi bi-check-lg"></i>
                    </a>
                </li>
                <li>
                    <a class="dropdown-item rounded fw-medium d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.sortOrder === 'asc'}" 
                       href="#" @click.prevent="setSort('asc')">
                       Oldest
                       <i v-if="taskStore.sortOrder === 'asc'" class="bi bi-check-lg"></i>
                    </a>
                </li>
            </ul>
        </div>

        <div class="dropdown position-relative" ref="filterDropdownRef">
            <button 
                class="btn bg-white border d-flex align-items-center shadow-sm hover-lift" 
                type="button" 
                @click="toggleFilter"
                style="border-radius: 8px; height: 40px; padding: 0 16px; transition: all 0.2s;"
            >
                <i class="bi bi-funnel text-muted me-2" style="font-size: 0.9rem;"></i>
                <span class="fw-medium text-dark" style="font-size: 0.85rem;">
                    {{ taskStore.statusFilter === 'All' ? 'Filters' : taskStore.statusFilter }}
                </span>
                <i class="bi bi-chevron-down ms-2 text-muted" style="font-size: 0.75rem;"></i>
            </button>
            <ul class="dropdown-menu dropdown-menu-end shadow border-0 mt-2" :class="{ show: isFilterOpen }" style="position: absolute; right: 0; top: 100%; border-radius: 12px; padding: 8px; min-width: 160px; font-size: 0.85rem; z-index: 1000;">
                <li>
                    <a class="dropdown-item rounded fw-medium mb-1 d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.statusFilter === 'All'}" 
                       href="#" @click.prevent="setFilter('All')">
                       All Status
                       <i v-if="taskStore.statusFilter === 'All'" class="bi bi-check-lg"></i>
                    </a>
                </li>
                <li>
                    <a class="dropdown-item rounded fw-medium mb-1 d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.statusFilter === 'Todo'}" 
                       href="#" @click.prevent="setFilter('Todo')">
                       Todo
                       <i v-if="taskStore.statusFilter === 'Todo'" class="bi bi-check-lg"></i>
                    </a>
                </li>
                <li>
                    <a class="dropdown-item rounded fw-medium mb-1 d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.statusFilter === 'In Progress'}" 
                       href="#" @click.prevent="setFilter('In Progress')">
                       In Progress
                       <i v-if="taskStore.statusFilter === 'In Progress'" class="bi bi-check-lg"></i>
                    </a>
                </li>
                <li>
                    <a class="dropdown-item rounded fw-medium d-flex align-items-center justify-content-between px-3 py-2" 
                       :class="{'bg-primary bg-opacity-10 text-primary': taskStore.statusFilter === 'Done'}" 
                       href="#" @click.prevent="setFilter('Done')">
                       Done
                       <i v-if="taskStore.statusFilter === 'Done'" class="bi bi-check-lg"></i>
                    </a>
                </li>
            </ul>
        </div>

        <button
            class="btn btn-primary d-flex align-items-center px-3 hover-lift shadow-sm fw-medium"
            @click="taskStore.openCreateModal()"
            style="height: 40px; border-radius: 6px; background-color: #4361ee; border-color: #4361ee; font-size: 0.9rem;"
        >
            <i class="bi bi-plus-lg me-2"></i>
            New Task
        </button>
    </div>
</div>

<LoadingSpinner
    v-if="taskStore.loading"
/>

<EmptyState
    v-else-if="taskStore.tasks.length==0"
/>

<TaskTable
    v-else
    :tasks="taskStore.filteredTasks"
/>

<!-- Modal di sini -->
<TaskFormModal/>
<TaskDetailModal/>

</div>

</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { useTaskStore } from "@/stores/taskStore"

import SearchBar from "@/components/task/SearchBar.vue"
import SummaryCards from "@/components/dashboard/SummaryCards.vue"
import LoadingSpinner from "@/components/common/LoadingSpinner.vue"
import EmptyState from "@/components/common/EmptyState.vue"
import TaskTable from "@/components/task/TaskTable.vue"
import TaskFormModal from "@/components/task/TaskFormModal.vue";
import TaskDetailModal from "@/components/task/TaskDetailModal.vue";

const taskStore = useTaskStore()
const currentDateTime = ref("")
const shortDateOnly = ref("")
const shortTimeOnly = ref("")
const sortDropdownRef = ref(null);
const filterDropdownRef = ref(null);

const isSortOpen = ref(false);
const isFilterOpen = ref(false);

const toggleSort = () => {
    isSortOpen.value = !isSortOpen.value;
};

const closeSort = () => {
    isSortOpen.value = false;
};

const setSort = (order) => {
    taskStore.sortOrder = order;
    closeSort();
};

const toggleFilter = () => {
    isFilterOpen.value = !isFilterOpen.value;
};

const closeFilter = () => {
    isFilterOpen.value = false;
};

const setFilter = (status) => {
    taskStore.statusFilter = status;
    closeFilter();
};

const handleClickOutside = (event) => {
    if (filterDropdownRef.value && !filterDropdownRef.value.contains(event.target)) {
        isFilterOpen.value = false;
    }
    if (sortDropdownRef.value && !sortDropdownRef.value.contains(event.target)) {
        isSortOpen.value = false;
    }
};

const updateDateTime = () => {
    const now = new Date();
    const optionsDate = { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Jakarta' };
    const dateStr = new Intl.DateTimeFormat('en-GB', optionsDate).format(now);
    
    const optionsTime = { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'Asia/Jakarta' };
    const timeStr = new Intl.DateTimeFormat('en-GB', optionsTime).format(now).replace(':', '.');
    
    currentDateTime.value = `${dateStr} ${timeStr}`;

    const optionsDateShort = { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'Asia/Jakarta' };
    const dateStrShort = new Intl.DateTimeFormat('en-GB', optionsDateShort).format(now);
    shortDateOnly.value = dateStrShort;
    shortTimeOnly.value = timeStr;
};

let timer
onMounted(async () => {
    updateDateTime()
    timer = setInterval(updateDateTime, 1000)
    await taskStore.fetchTasks()
    document.addEventListener("click", handleClickOutside);
})

onUnmounted(() => {
    clearInterval(timer)
    document.removeEventListener("click", handleClickOutside);
})
</script>

<style scoped>
.clock-pill {
    width: 100%;
}
@media (min-width: 768px) {
    .clock-pill {
        width: auto;
    }
}
</style>