<template>
    <div
        v-if="store.isModalOpen"
        class="modal fade show d-block"
        tabindex="-1"
        style="background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px);"
    >
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border-0 shadow-lg" style="border-radius: 16px; overflow: hidden; transform: translateY(0); animation: slideDown 0.3s ease-out forwards;">
                
                <!-- Modal Header -->
                <div class="modal-header border-bottom-0 pt-4 pb-0 px-4">
                    <h5 class="modal-title fw-bold d-flex align-items-center">
                        <div class="bg-primary bg-opacity-10 text-primary p-2 rounded-3 me-3 d-flex align-items-center justify-content-center" style="width: 40px; height: 40px;">
                            <i class="bi" :class="store.isEdit ? 'bi-pencil-square' : 'bi-plus-lg'"></i>
                        </div>
                        {{ store.isEdit ? "Edit Task" : "Create New Task" }}
                    </h5>
                    <button
                        type="button"
                        class="btn-close shadow-none"
                        @click="closeModal"
                    ></button>
                </div>

                <!-- Modal Body -->
                <div class="modal-body p-4">
                    <form @submit.prevent="saveTask">
                        
                        <!-- Title Input -->
                        <div class="mb-4">
                            <label class="form-label fw-semibold text-secondary tracking-wider">Task Title</label>
                            <input
                                v-model="form.title"
                                class="form-control bg-light border-0 shadow-none py-2 px-3"
                                style="border-radius: 10px;"
                                placeholder="What needs to be done?"
                                required
                            >
                        </div>

                        <!-- Description Input -->
                        <div class="mb-4">
                            <label class="form-label fw-semibold text-secondary  tracking-wider">Description</label>
                            <textarea
                                v-model="form.description"
                                class="form-control bg-light border-0 shadow-none py-2 px-3"
                                style="border-radius: 10px; resize: none;"
                                rows="3"
                                placeholder="Add more details about this task..."
                                maxlength="4000"
                            ></textarea>
                            <div class="text-end text-muted mt-1" style="font-size: 0.75rem;">
                                {{ form.description ? form.description.length : 0 }}/4000
                            </div>
                        </div>

                        <!-- Status Input -->
                        <div class="mb-4">
                            <label class="form-label fw-semibold text-secondary  tracking-wider">Status</label>
                            <select
                                v-model="form.status"
                                class="form-select bg-light border-0 shadow-none py-2 px-3"
                                style="border-radius: 10px; cursor: pointer;"
                            >
                                <option value="Todo">Todo</option>
                                <option value="In Progress">In Progress</option>
                                <option value="Done">Done</option>
                            </select>
                        </div>

                        <!-- Reminder Switch -->
                        <div class="form-check form-switch mb-3 d-flex align-items-center">
                            <input
                                id="remindCheck"
                                class="form-check-input mt-0 me-2"
                                type="checkbox"
                                v-model="form.remind_enabled"
                                :disabled="form.status === 'Done'"
                                style="cursor: pointer; width: 2.5em; height: 1.25em;"
                            >
                            <label class="form-check-label fw-medium" for="remindCheck" style="cursor: pointer;" :class="{'text-muted': form.status === 'Done'}">
                                Set a Reminder
                            </label>
                        </div>

                        <!-- Reminder Date Input -->
                        <div
                            v-if="form.remind_enabled"
                            class="mb-4 animate-fade-in"
                        >
                            <label class="form-label fw-semibold text-secondary tracking-wider">Reminder Date & Time</label>
                            <input
                                type="datetime-local"
                                class="form-control bg-light border-0 shadow-none py-2 px-3 text-primary fw-medium"
                                style="border-radius: 10px; cursor: pointer;"
                                v-model="form.remind_at"
                            >
                        </div>

                        <!-- Action Buttons -->
                        <div class="d-flex justify-content-end mt-4 pt-3 border-top">
                            <button
                                type="button"
                                class="btn btn-light me-2 px-4 py-2"
                                style="border-radius: 10px; font-weight: 500;"
                                @click="closeModal"
                            >
                                Cancel
                            </button>
                            <button
                                class="btn btn-primary px-4 py-2 hover-lift d-flex align-items-center"
                                style="border-radius: 10px; font-weight: 500;"
                                :disabled="store.saving"
                            >
                                <span
                                    v-if="store.saving"
                                    class="spinner-border spinner-border-sm me-2"
                                ></span>
                                <i v-else class="bi bi-check-lg me-2"></i>
                                {{ store.saving ? "Saving..." : "Save Task" }}
                            </button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-20px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
.tracking-wider {
    letter-spacing: 0.05em;
}
.form-switch .form-check-input:checked {
    background-color: var(--primary-color, #3b82f6);
    border-color: var(--primary-color, #3b82f6);
}

/* Make placeholder text more transparent */
input::placeholder,
textarea::placeholder {
    opacity: 0.5 !important;
}
</style>

<script setup>

import { reactive, watch } from "vue";
import { useTaskStore } from "@/stores/taskStore";

const store = useTaskStore();

const form = reactive({

    id: null,

    title: "",

    description: "",

    status: "Todo",

    remind_at: null,

    remind_enabled: false,

});

watch(

    () => store.selectedTask,

    (task) => {

        if(task){

            Object.assign(form, task);
            form.remind_enabled = !!task.remind_at;
            if (task.remind_at) {
                const date = new Date(task.remind_at);
                const tzOffset = date.getTimezoneOffset() * 60000;
                form.remind_at = new Date(date - tzOffset).toISOString().slice(0, 16);
            }

        }

        else{

            Object.assign(form,{

                id:null,

                title:"",

                description:"",

                status:"Todo",

                remind_at: null,

                remind_enabled: false

            });

        }

    },

    {

        immediate:true

    }

);

watch(
    () => form.status,
    (newStatus) => {
        if (newStatus === 'Done') {
            form.remind_enabled = false;
            form.remind_at = null;
        }
    }
);

function closeModal() {

    store.closeModal();

}

async function saveTask() {

    const payload = {

        title: form.title,

        description: form.description,

        status: form.status,

        remind_at: form.remind_enabled && form.remind_at
            ? new Date(form.remind_at).toISOString()
            : null

    };

    if (store.isEdit) {

        await store.updateTask(
            form.id,
            payload
        );

    }

    else {

        await store.createTask(payload);

    }

}

</script>