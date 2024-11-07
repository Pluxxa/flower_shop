document.addEventListener("DOMContentLoaded", function() {
    // Обработка клика по кнопке "Добавить в корзину"
    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", function() {
            alert("Товар добавлен в корзину!");
        });
    });

    // Обработка клика по кнопке "Быстрая покупка"
    document.querySelectorAll(".quick-buy").forEach(button => {
        button.addEventListener("click", function() {
            alert("Покупка завершена!");
        });
    });
});
