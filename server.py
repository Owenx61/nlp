#pip install flask
#pip install flask-cors

from flask import Flask, render_template, request
from flask_cors import CORS
import linker

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the file to a desired location
        file.save('uploads/' + file.filename)
        a=linker.main(request.form.get("questions"))
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)