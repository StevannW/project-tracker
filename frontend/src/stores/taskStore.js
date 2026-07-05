import { defineStore } from "pinia";
import taskService from "@/services/taskService";
import { successPopup } from "@/utils/toast";

export const useTaskStore = defineStore("task", {

    state: () => ({

        tasks: [],

        loading: false,

        saving: false,

        error: null,

        search: "",

        statusFilter: "All",

        sortOrder: "desc", // "desc" = Terbaru (Newest), "asc" = Terlama (Oldest)

        isModalOpen: false,
        isDetailModalOpen: false,
        isEdit: false,
        selectedTask: null
    }),
    getters: {
        filteredTasks(state) {
            let result = state.tasks.filter(task => {
                const matchSearch =
                    task.title
                        .toLowerCase()
                        .includes(state.search.toLowerCase());
                const matchStatus =
                    state.statusFilter === "All" ||
                    task.status === state.statusFilter;
                return matchSearch && matchStatus;
            });

            result.sort((a, b) => {
                return state.sortOrder === "desc" ? b.id - a.id : a.id - b.id;
            });

            return result;
        },
        totalTasks: (state) => state.tasks.length,
        todoCount: (state) =>
            state.tasks.filter(t => t.status === "Todo").length,
        progressCount: (state) =>
            state.tasks.filter(t => t.status === "In Progress").length,
        doneCount: (state) =>
            state.tasks.filter(t => t.status === "Done").length
    },
    actions: {
        async fetchTasks() {
            this.loading = true;
            this.error = null;
            try {
                const response = await taskService.getTasks();
                this.tasks = response.data;
            } catch (error) {
                console.error(error);
                this.error = "Failed to load tasks.";
            } finally {
                this.loading = false;
            }
        },
        async createTask(task) {
            this.saving = true;
            this.error = null;
            try {
                const response = await taskService.createTask(task);
                this.tasks.unshift(response.data);
                this.closeModal();
                successPopup("Task Created", "A new task has been successfully added.");
                return response.data;
            } catch (error) {
                console.error(error);
                this.error = "Failed to create task.";
                throw error;
            } finally {
                this.saving = false;
            }
        },
        async updateTask(id, task) {
            this.saving = true;
            this.error = null;
            try {
                const response =
                    await taskService.updateTask(id, task);
                const index =
                    this.tasks.findIndex(
                        t => t.id === id
                    );
                if (index !== -1) {
                    this.tasks[index] = response.data;
                }
                this.closeModal();
                successPopup("Task Updated", "The task has been successfully updated.");
                return response.data;
            } catch (error) {
                console.error(error);
                this.error = "Failed to update task.";
                throw error;
            } finally {
                this.saving = false;
            }
        },
        async deleteTask(id) {
            try {
                await taskService.deleteTask(id);
                this.tasks =
                    this.tasks.filter(
                        task => task.id !== id
                    );
                successPopup("Task Deleted", "The task has been deleted.");
            } catch (error) {
                console.error(error);
                this.error = "Failed to delete task.";
                throw error;
            }
        },
        openCreateModal() {
            this.isEdit = false;
            this.selectedTask = {
                title: "",
                description: "",
                status: "Todo"
            };
            this.isModalOpen = true;
        },
        openEditModal(task) {
            this.isEdit = true;
            this.selectedTask = { ...task };
            this.isModalOpen = true;
        },
        closeModal() {
            this.isModalOpen = false;
            this.selectedTask = null;
            this.isEdit = false;
        },
        openDetailModal(task) {
            this.selectedTask = { ...task };
            this.isDetailModalOpen = true;
        },
        closeDetailModal() {
            this.isDetailModalOpen = false;
            this.selectedTask = null;
        }
    }
});