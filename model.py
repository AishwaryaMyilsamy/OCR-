import cv2
import pytesseract
import numpy as np
from PIL import Image
from typing import Tuple

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def preprocess_image(image: Image) -> np.ndarray:
    #Pre-process the image to enhance text extraction.
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Use adaptive thresholding to create a binary image
    binary_image = cv2.adaptiveThreshold(
        blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    return binary_image

def extract_text_from_image(image: Image) -> str:
    #Extract text from the image using Tesseract OCR.
    preprocessed_image = preprocess_image(image)
    extracted_text = pytesseract.image_to_string(preprocessed_image, config='--psm 6')
    return extracted_text

def extract_meter_info(text: str) -> Tuple[str, str]:
    #Extract meter number and reading from text.
    # Implement a simple regex or string parsing to find the meter number and reading
    meter_number = ""
    meter_reading = ""

    # This example assumes meter numbers are numeric and have a fixed length (e.g., 10 digits)
    lines = text.split('\n')
    for line in lines:
        # Extract meter number based on expected format
        if len(line) >= 10 and line.isdigit():
            meter_number = line
        # Extract meter reading based on expected numeric format
        if any(char.isdigit() for char in line):
            meter_reading = line

    return meter_number, meter_reading
