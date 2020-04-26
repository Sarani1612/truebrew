$( document ).ready(function() {
    
    // gets divs containing user message dates and titles
    accordionBtn = document.querySelectorAll('.accordion-heading');

    // when clicking on an accordion-heading div, the toggleAccordion function is executed
    accordionBtn.forEach(button => button.addEventListener('click', toggleAccordion));

    // toggles showing the div containing the full message
    function toggleAccordion() {
        accordion = this.nextElementSibling;
        if (accordion.style.display === 'block') {
            accordion.style.display = 'none';
        } else {
            accordion.style.display = 'block';
        }
    };

});