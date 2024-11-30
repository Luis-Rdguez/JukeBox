document.addEventListener("DOMContentLoaded", function() {
    // Activa Select2 en todos los elementos <select> con la clase 'select2'
    const selectElements = document.querySelectorAll('.select2');
    selectElements.forEach(select => {
        $(select).select2({
            width: '100%',
            placeholder: select.getAttribute('data-placeholder') || 'Selecciona una opción',
            allowClear: true
        });
    });
});
