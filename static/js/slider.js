document.addEventListener('DOMContentLoaded', function() {
    const rangeInput = document.getElementById('priority');
    const rangeValue = document.getElementById('rangeValue');

    rangeInput.addEventListener('input', function() {
        rangeValue.textContent = rangeInput.value;
        console.log(rangeInput.value);
    });
});

