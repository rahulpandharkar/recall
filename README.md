# Facial Memory Application

A facial memory application that leverages Python's `face-recognition` library to recognize and recall faces in real-time using a webcam or an external camera. This project is ideal for exploring facial recognition technology in a simple yet effective way.  

## Table of Contents  

- [Introduction](#introduction)  
- [Prerequisites](#prerequisites)  
- [Usage](#usage)  
- [Features](#features)  
- [Documentation](#documentation)  
- [Notes](#notes)  
- [License](#license)  

## Introduction  

This application uses the `face-recognition` Python library for accurate facial detection and identification. It captures real-time video feed through a connected webcam, recognizes faces, and recalls previously seen faces.  

## Prerequisites  

1. **Web Camera**:  
   - Ensure your webcam is functional.  
   - Use external solutions like **DroidCam** if necessary.  

2. **Python**:  
   - Python 3.x installed on your system.  

3. **face-recognition Library**:  
   - Installable via pip. See the [face-recognition documentation](https://pypi.org/project/face-recognition/) for detailed setup instructions.  

## Usage  

1. Ensure prerequisites are all set.
2. Install the requirements using "requirements.txt"
3. Set up your Web Camera and check its port in the Python code (`recall.py`).  
4. Run the `recall.py` file to start the application.  

## Features  

- **Facial Recognition**:  
   - Detects and identifies faces using the `face-recognition` library.  
- **Memory Recall**:  
   - Recalls faces previously encountered by the application.  
- **Cross-Platform**:  
   - Compatible with Linux, Windows, and macOS systems.  

## Documentation  

For more information on the `face-recognition` library and its capabilities, refer to the official [face-recognition documentation](https://pypi.org/project/face-recognition/).  

## Notes  

- Ensure the camera is functional and permissions are enabled (if required by the operating system).  
- The application is a prototype and may require further optimization for handling larger datasets or environments.  

## License  

This project is open-source and free to use.  
