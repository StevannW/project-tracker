<template>
<div
    class="text-white d-flex flex-column shadow-lg sidebar"
    :class="{ 'collapsed': isCollapsed }"
    style="min-height:100vh; background: var(--sidebar-gradient);"
>
    <div class="p-4 border-bottom d-flex align-items-center justify-content-between position-relative">
        <div class="d-flex align-items-center overflow-hidden" style="white-space: nowrap;">
            <div class="bg-primary bg-opacity-25 p-2 rounded-3 me-3 d-flex align-items-center justify-content-center" style="min-width: 40px; height: 40px;">
                <i class="bi bi-kanban-fill text-primary"></i>
            </div>
            <h4 class="fw-bold mb-0 text-nowrap title-text" style="letter-spacing: -0.5px; opacity: 1; transition: opacity 0.2s;">
                Task Tracker
            </h4>
        </div>
        
        <!-- Toggle Button floating on the right edge -->
        <button class="toggle-btn d-none d-md-flex align-items-center justify-content-center" @click="isCollapsed = !isCollapsed">
            <i class="bi" :class="isCollapsed ? 'bi-chevron-right' : 'bi-chevron-left'"></i>
        </button>
    </div>

    <div class="p-3">
        <RouterLink to="/" class="sidebar-link">
            <i class="bi bi-speedometer2 me-3" style="font-size: 1.25rem;"></i>
            <span class="link-text">Dashboard</span>
        </RouterLink>

        <RouterLink to="/notifications" class="sidebar-link mt-2">
            <i class="bi bi-bell me-3" style="font-size: 1.25rem;"></i>
            <span class="link-text">Notification</span>
            <span
                v-if="notificationStore.unreadCount > 0"
                class="badge bg-danger ms-auto badge-pulse rounded-pill"
                :class="{ 'd-none': isCollapsed }"
            >
                {{ notificationStore.unreadCount }}
            </span>
            <!-- Show small dot if collapsed -->
            <span 
                v-if="notificationStore.unreadCount > 0 && isCollapsed"
                class="position-absolute translate-middle p-1 bg-danger border border-light rounded-circle"
                style="top: 15px; right: 15px;"
            >
                <span class="visually-hidden">New alerts</span>
            </span>
        </RouterLink>
    </div>
</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue"
import { useNotificationStore } from "@/stores/notificationStore"

const notificationStore = useNotificationStore()
const isCollapsed = ref(false)

const handleResize = () => {
    if (window.innerWidth < 768) {
        isCollapsed.value = true;
    } else {
        isCollapsed.value = false;
    }
};

onMounted(() => {
    notificationStore.startPolling();
    handleResize();
    window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
    window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
.sidebar {
    width: 260px;
    transition: width 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
}

.sidebar.collapsed {
    width: 88px;
}

.sidebar.collapsed .title-text,
.sidebar.collapsed .link-text {
    opacity: 0;
    width: 0;
    overflow: hidden;
    display: none;
}

.sidebar.collapsed .border-bottom {
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    justify-content: center !important;
}

/* Floating Toggle Button matching reference image */
.toggle-btn {
    position: absolute;
    right: -14px;
    top: 50%;
    transform: translateY(-50%);
    width: 28px;
    height: 28px;
    background-color: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 50%;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    z-index: 100;
    color: #6c757d;
    cursor: pointer;
    transition: all 0.2s ease;
    padding: 0;
}

.toggle-btn:hover {
    background-color: #f8f9fa;
    color: #495057;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.sidebar-link {
    display: flex;
    align-items: center;
    padding: 12px 18px;
    border-radius: 12px;
    color: #94a3b8;
    text-decoration: none;
    margin-bottom: 8px;
    font-weight: 500;
    transition: all var(--transition-speed) ease;
    border: 1px solid transparent;
    position: relative;
    white-space: nowrap;
}

.sidebar.collapsed .sidebar-link {
    padding: 12px;
    justify-content: center;
}

.sidebar.collapsed .sidebar-link i {
    margin-right: 0 !important;
}

.sidebar-link i {
    transition: transform var(--transition-speed);
}

.sidebar-link:hover {
    background: rgba(255, 255, 255, 0.05);
    color: #fff;
    transform: translateX(4px);
}

.sidebar.collapsed .sidebar-link:hover {
    transform: none;
    background: rgba(255, 255, 255, 0.1);
}

.router-link-active {
    background: var(--primary-gradient);
    color: #fff;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.25);
    border-color: rgba(255, 255, 255, 0.1);
}

.border-bottom {
    border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    position: relative;
}
</style>