<template>
<div class="task-list-container">
    <div class="d-flex flex-column">
        <TaskRow
            v-for="task in paginatedTasks"
            :key="task.id"
            :task="task"
        />
    </div>

    <div
        class="d-flex justify-content-between align-items-center mt-3"
        v-if="props.tasks.length > 0"
    >

    <div class="text-muted">

        Showing

        {{ showingFrom }}

        to

        {{ showingTo }}

        of

        {{ props.tasks.length }}

        entries

    </div>

    <nav>

        <ul class="pagination mb-0">

            <li
                class="page-item"
                :class="{ disabled: currentPage === 1 }"
            >

                <button
                    class="page-link"
                    @click="changePage(currentPage - 1)"
                    :disabled="currentPage === 1"
                >

                    Previous

                </button>

            </li>

            <li

                v-for="page in totalPages"

                :key="page"

                class="page-item"

                :class="{ active: page === currentPage }"

            >

                <button

                    class="page-link"

                    @click="changePage(page)"

                >

                    {{ page }}

                </button>

            </li>

            <li

                class="page-item"

                :class="{ disabled: currentPage === totalPages }"

            >

                <button

                    class="page-link"

                    @click="changePage(currentPage + 1)"

                    :disabled="currentPage === totalPages"

                >

                    Next

                </button>

            </li>

        </ul>

    </nav>

</div>
</div>
</template>

<script setup>

import { ref, computed } from "vue"
import TaskRow from "./TaskRow.vue"

const props = defineProps({

    tasks: Array

})

const currentPage = ref(1)

const perPage = 10

const totalPages = computed(() => {

    return Math.max(

        1,

        Math.ceil(props.tasks.length / perPage)

    );

});

const paginatedTasks = computed(() => {

    const start = (currentPage.value - 1) * perPage

    return props.tasks.slice(

        start,

        start + perPage

    )

})

const showingFrom = computed(() => {

    if (props.tasks.length === 0) {

        return 0;

    }

    return (currentPage.value - 1) * perPage + 1;

});

const showingTo = computed(() => {

    return Math.min(

        currentPage.value * perPage,

        props.tasks.length

    );

});

function changePage(page){

    currentPage.value = page

}

</script>