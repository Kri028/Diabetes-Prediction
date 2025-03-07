document.getElementById('predictionForm').addEventListener('submit', function() {
    document.getElementById('loader').style.visibility = 'visible';
});

function showToast(message) {
    const toast = document.getElementById('toastMessage');
    toast.textContent = message;
    toast.style.display = 'block';
    setTimeout(function() {
        toast.style.display = 'none';
    }, 3000);
}

const predictionResult = document.getElementById('predictionResult');
if (predictionResult) {
    const predictionText = predictionResult.textContent;
    if (predictionText.includes('No Diabetes')) {
        showToast('Congratulations, you don’t have Diabetes, you are healthy!');
    } else if (predictionText.includes('Diabetes')) {
        showToast('Unfortunately you have diabetes.');
    }
}
