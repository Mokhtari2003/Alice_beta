
$(document).ready(function() {
    $('#sendMessage').click(function() {
        var message = $('#userMessage').val();
        $('.chat-box').append('<div class="message">You: ' + message + '</div>');
        $('#userMessage').val('');
    });

    $('#logout').click(function() {
        alert('Logged out successfully!');
    });

    $('#toggleMode').click(function() {
        $('body').toggleClass('dark-mode');
        $('.navbar').toggleClass('navbar-light bg-light navbar-dark bg-dark');
    });
});