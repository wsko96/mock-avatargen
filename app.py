import os
import uuid;
from flask import Flask
from flask import request
from flask import send_file
from flask import abort

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><p>My Avatar API v1</p></html>"

@app.route('/api/my_avatar/v1/generate', methods=['POST'])
def generateMyAvatar():
    """
    A simple mock my_avatar API, accepting an image file and style option
    to generate an 3D Avatar asset bundle.
    """
    file = request.files['file']
    file_path = file.filename
    file_name, file_extension = os.path.splitext(file_path)
    base_name = file_name
    
    if '/' in base_name:
        base_name = base_name[base_name.rindex('/') + 1:]
    
    temp_input_file = f'data/temp/{base_name}{file_extension}'

    file.save(temp_input_file)
    style = request.form['style']

    temp_output_file = processAvatarAssetFile(temp_input_file, base_name, file_extension, style)

    return send_file(temp_output_file)

def processAvatarAssetFile(input_file, base_name, file_extension, style):
    """
    A mock implementation to generate an 3D Avatar asset bundle file
    by using the input_file and the style option.
    """
    output_file = f'data/mpar/{base_name}.glb'

    if os.access(output_file, os.O_RDONLY):
        return output_file
    
    abort(404)
    
