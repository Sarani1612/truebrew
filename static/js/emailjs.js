$(document).ready(function () {

    const contactForm = document.querySelector('#contact-form');

    function sendMessage() {

        const formData = {
            'user': contactForm.user.value,
            'email': contactForm.email.value,
            'subject': contactForm.title.value,
            'message': contactForm.message_body.value
        };

        emailjs.send("gmail", "TrueBrew", formData, user)
        .then(
            function(response) {
                alert("Success!", response);
                console.log("Success!", response);
            },
        // Alerts the user if form failed to send
        function(error) {
            alert("Form failed to submit. \r\n Response:\n " + JSON.stringify(err));
            console.log("Failed", error);
        });
        
        return false;
    }

    contactForm.addEventListener('submit', sendMessage);

})