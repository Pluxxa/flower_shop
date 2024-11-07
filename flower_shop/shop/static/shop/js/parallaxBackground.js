document.addEventListener("scroll", function() {
    const scrollPosition = window.scrollY; // Получаем текущую позицию прокрутки
    const background = document.querySelector('.header-background'); // Находим фон
    if (background) { // Проверка на наличие элемента
        background.style.transform = `translateY(${scrollPosition * 0.2}px)`; // Изменяем позицию фона
    }
});
