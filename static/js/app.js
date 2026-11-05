document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {
            const button = form.querySelector("button[type='submit']");

            if (button) {
                button.textContent = "Submitting...";
                button.disabled = true;
            }
        });
    }

    console.log("CodeNova Student Project Showcase loaded successfully!");
});