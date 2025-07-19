$(document).ready(function () {
    // Initialize sections
    $('#image-preview-section').hide();
    $('#loading-section').hide();
    $('#result-section').hide();
    
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').attr('src', e.target.result);
                $('#image-preview-section').fadeIn(400).addClass('fade-in');
                $('#upload-area').hide();
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    // Handle file selection
    $("#imageUpload").change(function () {
        $('#result-section').hide();
        readURL(this);
    });

    // Handle drag and drop
    $('#upload-area').on('dragover', function(e) {
        e.preventDefault();
        $(this).addClass('dragover');
    });

    $('#upload-area').on('dragleave', function(e) {
        e.preventDefault();
        $(this).removeClass('dragover');
    });

    $('#upload-area').on('drop', function(e) {
        e.preventDefault();
        $(this).removeClass('dragover');
        
        var files = e.originalEvent.dataTransfer.files;
        if (files.length > 0) {
            $('#imageUpload')[0].files = files;
            readURL($('#imageUpload')[0]);
        }
    });

    // Predict button click
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $('#image-preview-section').hide();
        $('#loading-section').fadeIn(400);

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Hide loading and show result
                $('#loading-section').hide();
                $('#result-text').html(data);
                $('#result-section').fadeIn(600).addClass('fade-in');
                console.log('Success!');
            },
            error: function(xhr, status, error) {
                $('#loading-section').hide();
                $('#result-text').html('<div class="alert alert-danger"><i class="fas fa-exclamation-triangle me-2"></i>Error: Unable to process the image. Please try again.</div>');
                $('#result-section').fadeIn(600);
                console.error('Error:', error);
            }
        });
    });

    // Add smooth scrolling to results
    $(document).on('DOMNodeInserted', '#result-section', function() {
        $('html, body').animate({
            scrollTop: $('#result-section').offset().top - 100
        }, 800);
    });
});

// Reset upload function
function resetUpload() {
    $('#imageUpload').val('');
    $('#image-preview-section').hide();
    $('#result-section').hide();
    $('#loading-section').hide();
    $('#upload-area').fadeIn(400);
}

// Add some interactive effects
$(document).ready(function() {
    // Add hover effects to feature cards
    $('.feature-card').hover(
        function() {
            $(this).find('.feature-icon i').addClass('fa-pulse');
        },
        function() {
            $(this).find('.feature-icon i').removeClass('fa-pulse');
        }
    );

    // Add click effect to buttons
    $('.btn').on('click', function() {
        $(this).addClass('clicked');
        setTimeout(() => {
            $(this).removeClass('clicked');
        }, 200);
    });
});
