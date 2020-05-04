$( document ).ready(function() {
    
    // gets divs to trigger accordion
    accordionBtn = document.querySelectorAll('.accordion-heading');

    // when clicking on an accordion-heading div, the toggleAccordion function is executed
    accordionBtn.forEach(button => button.addEventListener('click', toggleAccordion));

    // toggles showing the div containing more information
    function toggleAccordion() {
        accordion = this.nextElementSibling;
        if (accordion.style.display === 'block') {
            accordion.style.display = 'none';
        } else {
            accordion.style.display = 'block';
        }
    }

    // Removes alert messages after 5 seconds
    setTimeout(function () {
        $('.alert').fadeOut('slow');}, 5000
        );

});