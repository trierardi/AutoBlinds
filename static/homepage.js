$(document).ready(function() {
    // This code will run when the page loads.

    // Binds a click function to the blinds down button.
    // This runs whenever you click the button.
    $('#blinds-down').click(function() {
        // Makes a web request to the server for the /down URL.
        $('#status').text('Status: Moving blinds down...');
        $.get('/down', function(result) {
            if (result.success === 'true') {
                $('#status').text('Status: Successfully moved blinds down');
            }
            else {
                $('#status').text('Status: Command failed');
            }
        });
    });

    // Binds a click function to the blinds up button.
    // This runs whenever you click the button.
    $('#blinds-up').click(function() {
        // Makes a web request to the server for the /down URL.
        $('#status').text('Status: Moving blinds up...');
        $.get('/up', function(result) {
            if (result.success === 'true') {
                $('#status').text('Status: Successfully moved blinds up');
            }
            else {
                $('#status').text('Status: Command failed');
            }
        });
    });
});