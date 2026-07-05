import api from "@/api/axios";

export default {

    getTasks() {
        return api.get("/tasks/");
    },

    createTask(task) {
        return api.post("/tasks/", task);
    },

    updateTask(id, task) {
        return api.put(`/tasks/${id}`, task);
    },

    deleteTask(id) {
        return api.delete(`/tasks/${id}`);
    }

};