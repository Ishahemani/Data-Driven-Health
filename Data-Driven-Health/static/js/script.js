document.addEventListener('DOMContentLoaded', function() {
    const cancerRadio = document.getElementById('cancer');
    const checkRadio = document.getElementById('check');
    const cancerQuestions = document.getElementById('cancerQuestions');
    const checkQuestions = document.getElementById('checkQuestions');
    const familyCancerYesRadio = document.getElementById('familyCancerYes');
    const familyCancerNoRadio = document.getElementById('familyCancerNo');
    const smokingYesRadio = document.getElementById('smokingYes');
    const smokingNoRadio = document.getElementById('smokingNo'); 
    const drinkFrequencyRadios = document.querySelectorAll('input[name="drinkFrequency"]');
    const drinkQuestionsDiv = document.getElementById('drinkquestions');
    const obesityHistoryYesradio = document.getElementById('obesityHistoryYes');
    const obesityHistoryNoradio = document.getElementById('obesityHistoryNo');

    drinkFrequencyRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            if (this.value !== '1') {
                drinkQuestionsDiv.style.display = 'block';
            } else {
                drinkQuestionsDiv.style.display = 'none';
            }
        });
    });

    cancerRadio.addEventListener('change', function() {
        if (this.checked) {
            cancerQuestions.style.display = 'block';
            checkQuestions.style.display = 'none';
        }
    });

    checkRadio.addEventListener('change', function() {
        if (this.checked) {
            checkQuestions.style.display = 'block';
            cancerQuestions.style.display = 'none';
        }
    });

    familyCancerYesRadio.addEventListener('change', function() {
        const familyCancerQuestions = document.getElementById('familyCancerQuestions');
        if (this.checked) {
            familyCancerQuestions.style.display = 'block';
        } else {
            familyCancerQuestions.style.display = 'none';
        }
    });
    familyCancerNoRadio.addEventListener('change', function() { // New
        const familyCancerQuestions = document.getElementById('familyCancerQuestions');
        if (this.checked) {
            familyCancerQuestions.style.display = 'none';
        }
    });

    smokingYesRadio.addEventListener('change', function() {
        const smokingQuestions = document.getElementById('smokingQuestions');
        if (this.checked) {
            smokingQuestions.style.display = 'block';
        } else {
            smokingQuestions.style.display = 'none';
        }
    });

    smokingNoRadio.addEventListener('change', function() { // New
        const smokingQuestions = document.getElementById('smokingQuestions');
        if (this.checked) {
            smokingQuestions.style.display = 'none';
        }
    });

    obesityHistoryYesradio.addEventListener('change', function() {
        const obesity = document.getElementById('obesity');
        if (this.checked) {
            obesity.style.display = 'block';
        } else {
            obesity.style.display = 'none';
        }
    });

    obesityHistoryNoradio.addEventListener('change', function() { // New
        const obesity = document.getElementById('obesity');
        if (this.checked) {
            obesity.style.display = 'none';
        }
    });

});


