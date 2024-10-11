from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Set up route for homepage
@app.route('/')
def index():
    print("Rendering index.html")
    return render_template('R Scanner.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print("No file part")
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        print("No selected file")
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print("File saved at:", file_path)
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
