<template>

<span
:class="badgeClass"
>

{{ status }}

</span>

</template>

<script setup>

import { computed } from "vue";

const props =
defineProps({

    status:String

})

const badgeClass =
computed(()=>{

    switch(props.status){

        case "Todo":

            return "badge bg-secondary";

        case "In Progress":

            return "badge bg-warning text-dark";

        case "Done":

            return "badge bg-success";

        default:

            return "badge bg-primary";

    }

})

</script>