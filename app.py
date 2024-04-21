import time

from flask import Flask, request, send_file, render_template, redirect
import os
app = Flask(__name__)
script_path = "main.py"
path1 = ''
path2 = ''
path3 = os.path.join('uploads', "green.geojson")
check_upload = False
@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        path1 = os.path.join('uploads', file1.filename)
        path2 = os.path.join('uploads', file2.filename)
        file1.save(path1)
        file2.save(path2)
        file1.filename = 'blue.geojson'
        file2.filename = 'red.geojson'
        os.system(f"py gen_pic.py uploads\\{file1.filename} uploads\\{file2.filename} uploads\\green.geojson")
        exec(open(script_path).read(), {'blue_path': os.path.abspath(path1),
                                      'red_path': os.path.abspath(path2),
                                      'green_path': os.path.abspath(path3)})
        return send_file(path3, as_attachment=True)

    return render_template('index.html')
@app.route('/images', methods=['GET', 'POST'])
def show_images():
    #exec(open("gen_pic.py").read(), {'blue_path': os.path.abspath(os.path.join('uploads', "blue.geojson")),
    #                                'red_path': os.path.abspath(os.path.join('uploads', "red.geojson")),
    #                                'green_path': os.path.abspath(os.path.join('uploads', "green.geojson"))})
    return '''
    <!DOCTYPE html>
<html>
<head>
    <title>Изображения</title>
    <style>
        .image-container {
            text-align: center;
            margin: 20px auto;
        }
        .image-container img {
            width: 200px;
            height: auto;
        }
        .image-container .caption {
            font-size: 14px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="image-container">
        <img src="/static/red_photo.png" alt="Красный граф">
        <div class="caption">Красный граф: Изображение</div>
    </div>
    <div class="image-container">
        <img src="/static/blue_photo.png" alt="Синий граф">
        <div class="caption">Синий граф: Изображение</div>
    </div>
    <div class="image-container">
        <img src="/static/green_photo.png" alt="Зеленый граф">
        <div class="caption">Зеленый граф: Изображение</div>
    </div>
</body>
    '''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)