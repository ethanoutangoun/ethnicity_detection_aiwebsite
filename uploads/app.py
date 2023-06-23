from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import testmod  # replace with your actual module

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        try:
            f = request.files['file']
            name = request.form.get('name')
            safe_filename = secure_filename(f.filename)
            f.save(safe_filename)
            ethnicity_result = testmod.calculate(safe_filename, name)  # replace with your actual function
            os.remove(safe_filename)
            return f'Ethnicity result: {ethnicity_result}', 200
        except Exception as e:
            print(e, flush=True)  # log the exception to console
            return 'An error occurred while processing your request.', 500
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
