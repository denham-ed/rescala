$(document).ready(function () {
    // Initialize Tool Tips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });
    // Auto Remove Bootstrap Messages
    // From Code Institute's Django-Blog Walkthrough
    setTimeout(function(){
        let messages = document.getElementById("msg");
        let alert = new bootstrap.Alert(messages);
        alert.close();
    },3000);
});


