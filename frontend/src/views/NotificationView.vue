<template>

<div class="container py-4 animate-fade-in">

    <div class="d-flex flex-column flex-md-row justify-content-between align-items-start align-items-md-center mb-4 gap-3">
        <h3 class="fw-bold mb-0">
            <i class="bi bi-bell-fill text-primary me-2"></i>
            Notifications
        </h3>
        <button
            v-if="store.notifications.length > 0"
            class="btn btn-outline-danger d-flex align-items-center justify-content-center gap-2 px-3 py-2 rounded-3 fw-medium shadow-sm btn-responsive"
            style="font-size: 0.85rem; transition: all 0.2s;"
            @click="clearAll"
        >
            <i class="bi bi-trash3"></i>
            Delete All
        </button>
    </div>

    <div
        v-if="store.notifications.length==0"
        class="card hover-lift text-center py-5"
    >
        <div class="card-body">
            <i class="bi bi-bell-slash text-muted" style="font-size: 3rem;"></i>
            <h5 class="mt-3 text-muted">No notifications yet</h5>
        </div>
    </div>

    <div class="row">
        <div class="col-12" style="animation-delay: 0.1s;">
            <div
                v-for="notification in store.notifications"
                :key="notification.id"
                class="card mb-3 hover-lift border-0"
                :class="{
                    'bg-white': notification.is_read,
                    'border-primary bg-primary bg-opacity-10': !notification.is_read
                }"
                :style="!notification.is_read ? 'box-shadow: 0 4px 15px rgba(59, 130, 246, 0.15) !important; border-left: 4px solid #3b82f6 !important;' : ''"
                style="cursor:pointer; transition: all 0.2s ease-in-out;"
                @click="openNotification(notification)"
            >
                <div class="card-body p-4">
                    <div class="d-flex align-items-start">
                        <div class="me-3">
                            <div class="bg-primary bg-opacity-10 p-2 rounded-circle d-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">
                                <i class="bi bi-bell text-primary fs-5"></i>
                            </div>
                        </div>
                        <div class="flex-grow-1">
                            <div class="d-flex justify-content-between align-items-center mb-1">
                                <strong class="fs-5" :class="{'text-primary': !notification.is_read}">
                                    {{ notification.title }}
                                </strong>
                                <small class="text-muted d-flex align-items-center">
                                    <i class="bi bi-clock me-1"></i>
                                    {{ formatDate(notification.created_at) }}
                                </small>
                            </div>
                            <p class="mb-0 text-secondary" style="font-size: 0.95rem;">
                                <span class="d-md-none">{{ truncateText(notification.message, 30) }}</span>
                                <span class="d-none d-md-inline">{{ truncateText(notification.message, 60) }}</span>
                            </p>
                            <div class="mt-2" v-if="!notification.is_read">
                                <span class="badge bg-primary rounded-pill badge-pulse px-3 py-2">
                                    New
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

</template>

<script setup>

import { onMounted } from "vue";
import { useNotificationStore } from "@/stores/notificationStore"
import Swal from "sweetalert2";

const store =
    useNotificationStore()

onMounted(() => {

    store.fetchNotifications();

})

function formatDate(date){
    return new Date(date).toLocaleString()
}

function truncateText(text, length) {
    if (!text) return "";
    return text.length > length ? text.substring(0, length) + "....." : text;
}

async function openNotification(notification){

    if(!notification.is_read){

        await store.markAsRead(notification.id);

    }

}

async function clearAll(){

    const result = await Swal.fire({
        title: "Delete all notifications?",
        text: "This action cannot be undone.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#dc3545",
        cancelButtonColor: "#6c757d",
        confirmButtonText: "Yes, delete all",
        cancelButtonText: "Cancel"
    });

    if(result.isConfirmed){
        await store.clearNotifications();
        Swal.fire({
            title: "Deleted!",
            text: "All notifications have been cleared.",
            icon: "success",
            timer: 1500,
            showConfirmButton: false
        });
    }

}

</script>

<style scoped>
.btn-responsive {
    width: 100%;
}
@media (min-width: 768px) {
    .btn-responsive {
        width: auto !important;
    }
}
</style>