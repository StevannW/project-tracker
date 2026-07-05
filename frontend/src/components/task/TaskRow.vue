<template>
<div class="card border-0 shadow-sm rounded-4 mb-3 task-box" :style="{ zIndex: isDropdownOpen ? 100 : 'auto', position: 'relative' }">
    <div class="card-body p-3 p-md-4 d-flex align-items-center justify-content-between">
        
        <div class="d-flex align-items-start gap-3 gap-md-4">
            <div class="rounded-circle d-flex align-items-center justify-content-center flex-shrink-0 mt-1" :class="iconBgClass" style="width: 50px; height: 50px;">
                <i class="bi" :class="iconClass" :style="{ color: iconColor }" style="font-size: 1.5rem;"></i>
            </div>

            <div class="d-flex flex-column">
                <h6 class="fw-bold mb-1 text-dark" style="font-size: 1.1rem;">{{ task.title }}</h6>
                <span class="text-muted mb-2" style="font-size: 0.85rem;">
                    Created at {{ task.created_at ? formatDate(task.created_at) : '22 Agustus 2024' }}
                </span>
                
                <div class="d-flex align-items-center gap-3" style="font-size: 0.85rem; font-weight: 700; color: #2b2b2b;">
                    <span class="d-flex align-items-center gap-1" :style="{ color: iconColor }">
                        <i class="bi bi-flag-fill"></i> {{ task.status }}
                    </span>
                </div>
            </div>
        </div>

        <div class="dropdown position-relative" ref="dropdownRef">
            <button class="btn btn-link text-muted p-2" type="button" @click="toggleDropdown" style="text-decoration: none;">
                <i class="bi bi-three-dots-vertical" style="font-size: 1.3rem;"></i>
            </button>
            <ul class="dropdown-menu dropdown-menu-end shadow-sm border-0 rounded-3" :class="{ show: isDropdownOpen }" style="position: absolute; right: 0; top: 100%; z-index: 1000; min-width: 8rem;">
                <li><a class="dropdown-item py-2 fw-medium" href="#" @click.prevent="handleDetail"><i class="bi bi-eye text-primary me-2"></i> Detail</a></li>
                <li><a class="dropdown-item py-2 fw-medium" href="#" @click.prevent="handleEdit"><i class="bi bi-pencil text-warning me-2"></i> Edit</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item py-2 text-danger fw-medium" href="#" @click.prevent="handleDelete"><i class="bi bi-trash text-danger me-2"></i> Delete</a></li>
            </ul>
        </div>
        
    </div>
</div>
</template>

<script setup>
import { computed, ref, onMounted, onBeforeUnmount } from "vue";
import { useTaskStore } from "@/stores/taskStore";
import { confirmDelete } from "@/utils/confirm";

const props = defineProps({
    task: Object
});

const store = useTaskStore();
const isDropdownOpen = ref(false);
const dropdownRef = ref(null);

const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value;
};

const closeDropdown = () => {
    isDropdownOpen.value = false;
};

const handleClickOutside = (event) => {
    if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
        isDropdownOpen.value = false;
    }
};

onMounted(() => {
    document.addEventListener("click", handleClickOutside);
});

onBeforeUnmount(() => {
    document.removeEventListener("click", handleClickOutside);
});

function handleDetail() {
    closeDropdown();
    store.openDetailModal(props.task);
}

function handleEdit(){
    closeDropdown();
    store.openEditModal(props.task);
}

async function handleDelete(){
    closeDropdown();
    const result = await confirmDelete();
    if(!result.isConfirmed){
        return;
    }
    await store.deleteTask(props.task.id);
}

const iconBgClass = computed(() => {
    switch(props.task.status) {
        case "Todo": return "bg-primary bg-opacity-10";
        case "In Progress": return "bg-warning bg-opacity-10";
        case "Done": return "bg-success bg-opacity-10";
        default: return "bg-secondary bg-opacity-10";
    }
});

const iconColor = computed(() => {  
    switch(props.task.status) {
        case "Todo": return "#3b82f6"; 
        case "In Progress": return "#f59e0b"; 
        case "Done": return "#10b981"; 
        default: return "#6c757d"; 
    }
});

const iconClass = computed(() => {
    switch(props.task.status) {
        case "Todo": return "bi-calendar-minus";
        case "In Progress": return "bi-hourglass-split";
        case "Done": return "bi-check-circle";
        default: return "bi-list-task";
    }
});

const formatDate = (dateString) => {
    if (!dateString) return "";
    const date = new Date(dateString);
    if (isNaN(date)) return "22 August 2024";
    return new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);
};
</script>

<style scoped>
.task-box {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.task-box:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.05) !important;
}
</style>