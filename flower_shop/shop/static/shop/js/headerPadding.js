document.addEventListener("DOMContentLoaded", function() {
    const header = document.querySelector("header"); // Выбираем header
    const main = document.querySelector("main");     // Выбираем main

    // Функция для обновления отступа main на основе высоты header
    function updateMainPadding() {
        const headerHeight = header.offsetHeight;     // Определяем текущую высоту header
        main.style.paddingTop = `${headerHeight}px`;  // Устанавливаем отступ main равный высоте header
    }

    updateMainPadding(); // Устанавливаем отступ при загрузке страницы

    // Обновляем отступ при изменении размера окна
    window.addEventListener("resize", updateMainPadding);
});
