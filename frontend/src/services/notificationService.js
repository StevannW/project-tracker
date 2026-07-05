import api from "@/api/axios";

export default {

    getNotifications() {
        return api.get("/notifications");
    },

    markAsRead(id) {

        return api.patch(`/notifications/${id}/read`);

    },
    clearNotifications() {

        return api.delete("/notifications/clear");

    },

}