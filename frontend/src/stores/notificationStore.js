import { defineStore } from "pinia";
import notificationService from "@/services/notificationService";

export const useNotificationStore = defineStore("notification", {

    state: () => ({

        notifications: [],

        loading: false,

        timer: null

    }),

    getters: {

        unreadCount(state) {

            return state.notifications.filter(

                n => !n.is_read

            ).length;

        }

    },

    actions: {

        async fetchNotifications() {

            this.loading = true;

            try {

                const response =
                    await notificationService.getNotifications();

                this.notifications =
                    response.data;

            }

            finally {

                this.loading = false;

            }

        },

        startPolling() {

            this.fetchNotifications();

            if (this.timer) {

                clearInterval(this.timer);

            }

            this.timer = setInterval(() => {

                this.fetchNotifications();

            }, 5000);

        },

        stopPolling() {

            if (this.timer) {

                clearInterval(this.timer);

                this.timer = null;

            }

        },

        async markAsRead(id) {

            await notificationService.markAsRead(id);

            await this.fetchNotifications();

        },
        async clearNotifications() {

            await notificationService.clearNotifications();

            this.notifications = [];

        }

    }

});