import Swal from "sweetalert2";

export async function confirmDelete() {

    return Swal.fire({

        title: "Delete Task?",

        text: "This action cannot be undone.",

        icon: "warning",

        showCancelButton: true,

        confirmButtonText: "Delete",

        cancelButtonText: "Cancel",

        confirmButtonColor: "#dc3545"

    });

}