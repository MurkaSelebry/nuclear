from flask import Flask, request, send_file
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        # Здесь можно добавить логику обработки файлов
        # Например, объединение файлов или их преобразование
        # В данном примере мы просто сохраняем файлы и возвращаем их обратно
        file1.save(os.path.join('uploads', file1.filename))
        file2.save(os.path.join('uploads', file2.filename))

        # Предположим, что третий файл - это просто один из входных файлов
        # В реальном приложении здесь должна быть логика обработки файлов
        return send_file(os.path.join('uploads', file1.filename), as_attachment=True)
    return '''
    <!doctype html>
    <html>
    <body>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file1>
      <input type=file name=file2>
      <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
