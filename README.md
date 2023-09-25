# Steganography Python Script + Web UI

This is a simple Python script that can be utilised from a PHP backend that allows users to encode and decode hidden messages within images using steganography. Steganography is the practice of concealing a message, file, or data within another file, message, or data.

## Overview

This web application consists of multiple PHP and Python files that work together to provide an intuitive user interface for steganography operations. Users can upload an image, enter a message, and choose between encoding and decoding operations. The encoding process hides the message within the image, while the decoding process retrieves the hidden message from an encoded image.

## Files

### 1. `index.php`

- The main entry point of the web application.
- Provides options to navigate to the encoding and decoding pages.

### 2. `encode.php`

- Allows users to upload an image.
- Displays information about the uploaded image, including size, type, resolution, and maximum character capacity for encoding.
- Provides an input field for entering the message to be encoded.

### 3. `deliver.php`

- Handles the encoding process.
- Accepts the uploaded image and message.
- Executes the `steganography.py` script to encode the message into the image.
- Displays the encoded image and provides a download link.

### 4. `steganography.py`

- The Python script responsible for the steganography encoding and decoding operations.
- Provides `Steganography` class for encoding and decoding messages within images.
- Offers command-line functionality for encoding and decoding images.
- Utilizes the Pillow (PIL) library for image manipulation.

## Usage

1. **Running the Application:**

   - Place the folder in <XAMPPInstallation>\htdocs\<folderName>
   - Make sure python is installed and the path to python.exe is changed in 'delivery.php'.
   - Install PIL / Pillow library. (python -m pip install pillow)

2. **Accessing the Application:**

   - Open a web browser and navigate to the URL where the web application is hosted (e.g., `http://localhost/`).

3. **Encoding a Message:**

   - Click on the "Encode" option on the main page.
   - Upload an image and enter a message.
   - Click "Upload" to initiate the encoding process.

4. **Decoding a Message:**

   - Click on the "Decode" option on the main page.
   - Upload an encoded image to retrieve the hidden message.

## Dependencies

- PHP for server-side scripting.
- Tested on XAMPP Server (No Settings Were Changed)
- Bootstrap CSS and JavaScript for styling and layout.
- Pillow (PIL) library for image manipulation in the Python script.

## Configuration

- Ensure that the path to the Python executable (`python.exe`) in `steganography.py` is correctly set.
- Configure the `steganography.py` script as needed for your steganography requirements.

## Author

- Sreyas Cheeran Velikoth

Feel free to modify and enhance this web application for your specific use case.
