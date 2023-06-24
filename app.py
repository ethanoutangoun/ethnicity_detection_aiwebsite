from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
import cropping
import csv_mod
import clarifai
import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

@app.route('/')
def upload_file():
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_post():
   if request.method == 'POST':
      firstName = request.form.get('firstName')  # Retrieve the first name from the form
      lastName = request.form.get('lastName')  # Retrieve the last name from the form

      f = request.files['file']
      filename = secure_filename(f.filename)
      #print(filename)

      

      f.save(os.path.join("uploads", filename))
      path = "./uploads/" + filename
      cropping.crop_largest_face(path)#function is hardcoded to save cropped image to uploads folder
      
      csv_mod.create_csv(firstName,lastName,"./uploads/cropped.jpg", "./uploads")
      
      clarifai.main()

      #Open inferences file
      with open("inferences.csv", "r") as f:
         reader = csv.reader(f)
         next(reader)
         row = next(reader)
         race = (row[6])


      #return 'Hello {}, file {} uploaded successfully'.format(name, filename)
      return render_template('uploaded.html', firstName=firstName, lastName = lastName, race = race, filename=filename)


@app.route('/uploads/<filename>')
def send_file(filename):
   return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
   app.run(debug = True)
