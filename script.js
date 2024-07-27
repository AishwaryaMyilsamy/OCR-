document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('image-input');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    fetch('/extract', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('meter-number').textContent = data.meter_number;
            document.getElementById('meter-reading').textContent = data.meter_reading;
            document.getElementById('result').style.display = 'block';
        }
    })
    .catch(error => console.error('Error:', error));
});
