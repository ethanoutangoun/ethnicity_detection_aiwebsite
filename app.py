from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
import cropping

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

@app.route('/')
def upload_file():
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_post():
   if request.method == 'POST':
      name = request.form.get('name')  # Retrieve the name from the form
      f = request.files['file']
      filename = secure_filename(f.filename)
      #print(filename)

      

      f.save(os.path.join("uploads", filename))
      path = "./uploads/" + filename
      cropping.crop_largest_face(path)#function is hardcoded to save cropped image to uploads folder
    


      #return 'Hello {}, file {} uploaded successfully'.format(name, filename)
      return render_template('uploaded.html', name=name, filename="cropped.jpg")


@app.route('/uploads/<filename>')
def send_file(filename):
   return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
   app.run(debug = True)
