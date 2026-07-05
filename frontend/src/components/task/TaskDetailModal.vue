<template>
<div class="modal fade" id="taskDetailModal" tabindex="-1" aria-hidden="true" ref="modalRef">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
            <div class="modal-header border-0 bg-light pb-2 pt-4 px-4">
                <h5 class="modal-title fw-bold text-dark">Task Details</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="closeModal"></button>
            </div>
            
            <div class="modal-body px-4 pt-3 pb-4" v-if="task">
                <div class="mb-4">
                    <h4 class="fw-bold text-dark mb-1">{{ task.title }}</h4>
                    <div class="d-flex align-items-center gap-2 mt-2">
                        <span class="badge rounded-pill fw-medium px-3 py-2" :class="badgeClass" style="font-size: 0.75rem; letter-spacing: 0.5px;">
                            {{ task.status }}
                        </span>
                        <span class="text-muted" style="font-size: 0.8rem;" v-if="task.remind_at">
                            <i class="bi bi-alarm me-1"></i>
                            Remind me at {{ formatDateTime(task.remind_at) }}
                        </span>
                        <span class="text-muted" style="font-size: 0.8rem;" v-else>
                            <i class="bi bi-alarm-fill me-1"></i>
                            No reminder set
                        </span>
                    </div>
                </div>
                
                <div class="mb-3">
                    <label class="form-label text-muted fw-bold text-uppercase" style="font-size: 0.7rem; letter-spacing: 1px;">Description</label>
                    <div class="p-3 bg-light rounded-3 text-dark" style="font-size: 0.9rem; min-height: 80px; white-space: pre-wrap;">
                        {{ task.description || 'No description provided.' }}
                    </div>
                </div>
            </div>
            
            <div class="modal-footer border-0 px-4 pb-4 pt-0">
                <button type="button" class="btn btn-light rounded-3 px-4 fw-medium" data-bs-dismiss="modal" @click="closeModal">Close</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { useTaskStore } from "@/stores/taskStore";
import * as bootstrap from "bootstrap";

const store = useTaskStore();
const modalRef = ref(null);
let modalInstance = null;

const task = computed(() => store.selectedTask);

onMounted(() => {
    modalInstance = new bootstrap.Modal(modalRef.value, {
        backdrop: 'static'
    });
    
    modalRef.value.addEventListener('hidden.bs.modal', () => {
        if (store.isDetailModalOpen) {
            store.closeDetailModal();
        }
    });
});

watch(() => store.isDetailModalOpen, (isOpen) => {
    if (isOpen) {
        modalInstance?.show();
    } else {
        modalInstance?.hide();
    }
});

const closeModal = () => {
    store.closeDetailModal();
};

const badgeClass = computed(() => {
    if (!task.value) return "";
    switch (task.value.status) {
        case "Todo":
            return "bg-primary bg-opacity-10 text-primary border border-primary border-opacity-25";
        case "In Progress":
            return "bg-warning bg-opacity-10 text-warning border border-warning border-opacity-25";
        case "Done":
            return "bg-success bg-opacity-10 text-success border border-success border-opacity-25";
        default:
            return "bg-secondary bg-opacity-10 text-secondary border border-secondary border-opacity-25";
    }
});

const formatDateTime = (dateString) => {
    if (!dateString) return "";
    const date = new Date(dateString);
    const datePart = new Intl.DateTimeFormat('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);
    const timePart = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'Asia/Jakarta' }).format(date).replace(':', '.');
    return `${datePart}, ${timePart}`;
};
</script>
