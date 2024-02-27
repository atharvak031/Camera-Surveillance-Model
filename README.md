
# Suspicious Activity Detection Model
The project is a web-based application designed for detecting suspicious activities within uploaded videos. It utilizes Flask, a micro web framework for Python, to provide a user-friendly interface for uploading videos and receiving analysis results. The core functionality of the application is powered by TensorFlow, an open-source machine learning framework, which employs a pre-trained DenseNet121 model for video classification.

Upon uploading a video file, the application preprocesses the video frames, extracts features using the DenseNet121 model, and classifies the video based on these features. The classification result is determined by comparing predictions against a predefined threshold. If the prediction exceeds the threshold, the application indicates that the video contains suspicious activity; otherwise, it reports that no suspicious activity is detected.

The codebase is structured into modular functions responsible for loading the model, preprocessing video frames, and classifying videos. Additionally, the application includes routes for rendering HTML templates (such as the home page and result page) and handling file uploads.





## Features

- Upload video files for analysis.
- Automated detection of suspicious activities within uploaded videos.
- User-defined threshold for determining suspicious behavior.
- Simple web-based interface for ease of use.


## Requirements
- Python 3.x 
- Flask
- OpenCV
- Numpy
- TensorFlow
- Pre-trained model files

Note: As of creation of this readme file, the latest version of Python that Tensorflow supports is 3.11, any version above 3.11 will have trouble detecting the library. Therefore, make sure to check for this discrepancy.

Make sure your local machine has enough computation power to run the program. The model was executed on a machine with 8GB of RAM and on an Intel Core i5 processor. Also, use a stable internet connection for seamless usage.
## Installation

- For installing Flask:
```bash
pip install Flask
```

- For installing OpenCV:
```bash
pip install opencv-python-headless
```

- For installing Tensorflow:
```bash
pip install tensorflow
```

- After installing the libraries, check whether the file path for loading the model is correct or not.

- For loading model:
```bash
#Change the file path inside the quotes (use finalweights.h5 file)
model = tf.keras.models.load_model('filepath')
```

- Now, run the program using the following command in the terminal:
```bash
flask run
```
- Observe the terminal of the program, once it specifies that you can exit the program using Ctrl+C, it means that the program is running successfully.





## Usage

- Access the application by opening a web browser and navigating to http://localhost:5000
- Click on the "Choose File" button to select the video file you want to analyze.
- Once the file is selected, click on the "Upload" button to start the analysis process and wait for the analysis to complete.
- The system will display the result indicating whether suspicious activity is detected in the uploaded video.




## Instructions For Developers

- The model depends entirely on the kind of data being used for training it and on the number of epochs it has been trained for. 
- Always make sure that you are training the model on relevant data and testing it thoroughly. Experiment with the threshold value to determine the best possible value that can be used. 
- For further addition of features like classification, use labelled data.
- If the model is being trained on the client's data, consider skipping the pre-processing part of the model which takes a chunk of the processing time and test the model on the client's data itself making it more customised.
- You will have to make changes for CUDA based GPU's in the program.
- Train the model on high resolution images with enough computation power, so that the feature extraction of the model works perfectly. 
## Acknowledgements

 - [Training and Testing Data taken from this website](https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABvnJSwZI7zXb8_myBA0CLHa?dl=0)
