# app.py
from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import base64
from model import extract_text_from_image, extract_meter_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    image = Image.open(file.stream)

    # Extract text from image
    extracted_text = extract_text_from_image(image)
    meter_number, meter_reading = extract_meter_info(extracted_text)

    return jsonify({'meter_number': meter_number, 'meter_reading': meter_reading})

if __name__ == '__main__':
    app.run(debug=True)

