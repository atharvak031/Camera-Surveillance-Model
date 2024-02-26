from flask import Flask, render_template, request
import os
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Define your model loading function
def load_model():
    # Define your model architecture
    def create_model():
        inputs = tf.keras.layers.Input(shape=(320, 240, 3))
        feature_extractor = tf.keras.applications.DenseNet121(
            include_top=False, weights="imagenet", input_tensor=inputs
        )
        feature_extractor.trainable = False

        x = tf.keras.layers.GlobalAveragePooling2D()(feature_extractor.output)
        x = tf.keras.layers.Dense(256, activation="relu")(x)
        x = tf.keras.layers.Dropout(0.3)(x)
        x = tf.keras.layers.Dense(1024, activation="relu")(x)
        x = tf.keras.layers.Dropout(0.5)(x)
        x = tf.keras.layers.Dense(512, activation="relu")(x)
        x = tf.keras.layers.Dropout(0.4)(x)
        outputs = tf.keras.layers.Dense(3, activation="softmax", name="classification")(x)

        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        return model

    # Create an instance of the model
    #This is the path for loading the model, make sure that this path is correct 
    model = tf.keras.models.load_model('D:\Documents\Cling Internship Documents\Suspicious_Activity_Detection_Model\venv\model')
    return model

# Load the model
model = load_model()
model.summary()

# Define functions for video processing
def preprocess_video(video_path, max_frames=0, resize=(240, 320)):
    cap = cv2.VideoCapture(video_path)
    frames = []

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = crop_center_square(frame)
            frame = cv2.resize(frame, resize)
            frame = preprocess_frame(frame)
            frames.append(frame)

            if max_frames > 0 and len(frames) == max_frames:
                break
    finally:
        cap.release()

    return np.array(frames)

def crop_center_square(frame):
    y, x = frame.shape[0:2]
    min_dim = min(y, x)
    start_x = (x // 2) - (min_dim // 2)
    start_y = (y // 2) - (min_dim // 2)
    return frame[start_y:start_y+min_dim, start_x:start_x+min_dim, :]

def preprocess_frame(frame):
    frame = frame[:, :, [2, 1, 0]]
    frame = frame / 255.0
    return frame

def classify_video(predictions, threshold):
    if np.max(predictions) > threshold:
        return "The video contains suspicious activity."
    else:
        return "The video does not contain suspicious activity."

# Set up Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if file:
        # Save the uploaded file to a temporary location
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        # Process the uploaded video
        video_frames = preprocess_video(file_path)
        predictions = model.predict(video_frames)

        # Assuming you have a threshold for classifying violent activity
        threshold = 0.5  # Set your threshold here

        # Determine if the video contains violent activity based on predictions and threshold
        result = classify_video(predictions, threshold)

        # Remove the temporary file
        os.remove(file_path)

        return render_template("result.html", result=result)

    return "Something went wrong."

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)