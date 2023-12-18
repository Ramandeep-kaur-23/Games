const carousel = document.querySelector(".carousel");

const dragging = (e) => {
    carousel.scrollLeft = e.pagex;
}

carousel.addEventListener("mousemove", dragging);