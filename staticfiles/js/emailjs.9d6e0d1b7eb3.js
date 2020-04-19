$(document).ready(function () {

    const contactForm = document.querySelector('#contact-form');

    function sendMessage() {

        var data = {
            service_id: 'gmail',
            template_id: 'TrueBrew',
            user_id: user,
            template_params: {
                'user': contactForm.user.value,
                'email': contactForm.email.value,
                'subject': contactForm.title.value,
                'message': contactForm.message_body.value
            }
        };

        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json'
        }).done(function () {
            alert('Your message was sent');
            console.log('Success');
        }).fail(function (error) {
            alert('Oops... ' + JSON.stringify(error));
            console.log('Oops...');
        });

    }

    contactForm.addEventListener('submit', sendMessage);

})