document.addEventListener("DOMContentLoaded", function() {
    let lastScrollPosition = 0;
    const header = document.querySelector("header");

    window.addEventListener("scroll", function() {
        const currentScrollPosition = window.scrollY;

        if (currentScrollPosition > lastScrollPosition) {
        // Прокрутка вниз, скрываем шапку
            header.classList.add("hide-header");
        } else {
                // Прокрутка вверх, показываем шапку
            header.classList.remove("hide-header");
        }

            // Обновляем позицию последней прокрутки
        lastScrollPosition = currentScrollPosition;
    });
});

