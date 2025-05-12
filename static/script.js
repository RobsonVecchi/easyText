document.addEventListener("DOMContentLoaded", () => {
    window.copiarTexto = function(texto, titulo) {
        navigator.clipboard.writeText(texto)
            .then(() => {
                const toastElement = document.getElementById("toast");
                const toastBody = document.getElementById("toast-body");
                toastBody.textContent = `Texto "${titulo}" copiado!`;
                const toast = new bootstrap.Toast(toastElement);
                toast.show();
            })
            .catch(err => {
                console.error("Erro ao copiar texto:", err);
            });
    };
});
