document.addEventListener('DOMContentLoaded', () => {
    const drawer = document.getElementById("edit-drawer");
    const gear = document.getElementById("edit-gear");
    const closeBtn = document.getElementById("close-drawer");
    const swapButtons = document.querySelectorAll(".swap-btn");

    gear.addEventListener("click", () => {
        drawer.classList.add("visible");
    });

    closeBtn.addEventListener("click", () => {
        drawer.classList.remove("visible");
    });

    swapButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const target = btn.dataset.target;
            const src = btn.dataset.src;
            const elem = document.getElementById(`furniture-${target}`);
            if (!elem) return;

            elem.src = `/static/images/${src}`;
        });
    });


});
