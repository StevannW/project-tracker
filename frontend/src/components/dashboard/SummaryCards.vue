<template>

<div class="row g-3 mb-4 animate-fade-in" style="animation-delay: 0.1s;">

    <div class="col-md-3">
        <div class="card hover-lift h-100" style="border-left: 4px solid #6c757d !important;">
            <div class="card-body p-3">
                <div class="d-flex justify-content-between align-items-center mb-1">
                    <span class="text-muted fw-semibold" style="font-size: 0.85rem;">Total Task</span>
                    <div class="bg-secondary bg-opacity-10 rounded text-secondary d-flex align-items-center justify-content-center" style="width: 30px; height: 30px;">
                        <i class="bi bi-list-task"></i>
                    </div>
                </div>
                <div class="fs-4 fw-bold text-dark">{{ store.totalTasks }}</div>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card hover-lift h-100" style="border-left: 4px solid #3b82f6 !important;">
            <div class="card-body p-3">
                <div class="d-flex justify-content-between align-items-center mb-1">
                    <span class="text-muted fw-semibold" style="font-size: 0.85rem;">Todo</span>
                    <div class="bg-primary bg-opacity-10 rounded text-primary d-flex align-items-center justify-content-center" style="width: 30px; height: 30px;">
                        <i class="bi bi-calendar-minus"></i>
                    </div>
                </div>
                <div class="fs-4 fw-bold text-primary">{{ store.todoCount }}</div>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card hover-lift h-100" style="border-left: 4px solid #f59e0b !important;">
            <div class="card-body p-3">
                <div class="d-flex justify-content-between align-items-center mb-1">
                    <span class="text-muted fw-semibold" style="font-size: 0.85rem;">In Progress</span>
                    <div class="bg-warning bg-opacity-10 rounded text-warning d-flex align-items-center justify-content-center" style="width: 30px; height: 30px;">
                        <i class="bi bi-hourglass-split"></i>
                    </div>
                </div>
                <div class="fs-4 fw-bold text-warning">{{ store.progressCount }}</div>
            </div>
        </div>
    </div>

    <div class="col-md-3">
        <div class="card hover-lift h-100" style="border-left: 4px solid #10b981 !important;">
            <div class="card-body p-3">
                <div class="d-flex justify-content-between align-items-center mb-1">
                    <span class="text-muted fw-semibold" style="font-size: 0.85rem;">Done</span>
                    <div class="bg-success bg-opacity-10 rounded text-success d-flex align-items-center justify-content-center" style="width: 30px; height: 30px;">
                        <i class="bi bi-check-circle"></i>
                    </div>
                </div>
                <div class="fs-4 fw-bold text-success">{{ store.doneCount }}</div>
            </div>
        </div>
    </div>

</div>

</template>

<script setup>

import { useTaskStore } from "@/stores/taskStore";

const store = useTaskStore();

</script>