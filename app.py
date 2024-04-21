import time

from flask import Flask, request, send_file, render_template, redirect
import os
app = Flask(__name__)
script_path = "main.py"
path3 = os.path.join('uploads', "green.geojson")

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        path1 = os.path.join('uploads', file1.filename)
        path2 = os.path.join('uploads', file2.filename)
        file1.save(path1)
        file2.save(path2)
        exec(open(script_path).read(), {'blue_path': os.path.abspath(path1),
                                      'red_path': os.path.abspath(path2),
                                      'green_path': os.path.abspath(path3)})
        send_file(path3, as_attachment=True)
        return redirect('/images')
    return render_template('index.html')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)