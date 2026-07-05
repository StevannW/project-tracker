import Swal from "sweetalert2";

export function successToast(message) {

    Swal.fire({

        toast: true,

        position: "top-end",

        timer: 2000,

        showConfirmButton: false,

        icon: "success",

        title: message

    });

}

export function successPopup(title, text = "") {
    Swal.fire({
        icon: "success",
        title: title,
        text: text,
        timer: 2000,
        showConfirmButton: false
    });
}

export function errorToast(message) {

    Swal.fire({

        toast: true,

        position: "top-end",

        timer: 3000,

        showConfirmButton: false,

        icon: "error",

        title: message

    });

}