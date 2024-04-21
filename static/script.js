document.addEventListener('DOMContentLoaded', function() {
    const fileInputs = document.querySelectorAll('.custom-file-input');
    const uploadBtn = document.querySelector('.upload-btn');
    const checkbox = document.getElementById('flexCheckDefault');

    fileInputs.forEach(function(input, index) {
        input.addEventListener('change', function() {
            const fileName = this.files[0].name;
            const extension = fileName.split('.').pop().toLowerCase();
            const label = this.nextElementSibling;

            // Проверяем расширение файла
            if (extension === 'json' || extension === 'geojson') {
                label.innerText = fileName;

                // Проверяем условия для активации кнопки
                if (fileInputs[0].value && fileInputs[1].value && checkbox.checked) {
                    uploadBtn.classList.add('active');
                    uploadBtn.disabled = false;
                } else {
                    uploadBtn.classList.remove('active');
                    uploadBtn.disabled = true;
                }
            } else {
                // Если файл не JSON или GeoJSON, сбрасываем значение и отключаем кнопку
                this.value = ''; // Сброс значения input
                label.innerText = 'Choose file ' + (index + 1);
                uploadBtn.classList.remove('active');
                uploadBtn.disabled = true;
                alert('Please upload only JSON or GeoJSON files.');
            }
        });
    });

    // Добавляем проверку перед загрузкой
    uploadBtn.addEventListener('click', function() {
        if (!checkbox.checked) {
            alert("Please check 'I want to upload files' before uploading.");
        }
    });

    checkbox.addEventListener('change', function() {
        if (this.checked && fileInputs[0].value && fileInputs[1].value) {
            uploadBtn.classList.add('active');
            uploadBtn.disabled = false;
        } else {
            uploadBtn.classList.remove('active');
            uploadBtn.disabled = true;
        }
    });

    document.querySelector('form').addEventListener('submit', function(e) {
        document.querySelector('.loading-overlay').style.display = 'flex';
    });
    uploadBtn.addEventListener('click', function() {
        document.getElementById('loading-overlay').style.display = 'none';
    });
});
