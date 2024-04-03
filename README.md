# Heart Disease Predictor

## Overview
Heart Disease Predictor is a web application that predicts the likelihood of heart disease based on various input parameters. It includes a FastAPI backend for making predictions and a frontend interface for user interaction. try it? : URL: https://heart-disease-detector-5ykjaaunx-my-team70.vercel.app
as the hosting of the api is free, (the API automatically shuts down or delays the calls by 50 - 60 seconds)


## Features
- Accepts user input data through a web form.
- Predicts the likelihood of heart disease using a pre-trained machine learning model.
- Stores prediction results and user input data in a MongoDB database.
- Provides a simple frontend interface for users to interact with.
- integration of fastapi for versetality

## Usage
To run the project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/nimo-codes/Heart-Disease-Detector-Frontend-API-ML-.git
   ```

2. Navigate to the project directory:
   ```bash
   cd heart-disease-predictor
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the frontend interface at http://localhost:8000.

## Hosted API
- **API Endpoint:** [https://heartdiseaseapi-ixmu.onrender.com/predict](https://heartdiseaseapi-ixmu.onrender.com/predict)
- **Description:** Hosted FastAPI endpoint for making predictions.
- **Usage:** Send a POST request with input data in JSON format to receive prediction results.

## Hosted Website
- **URL:** [https://heart-disease-detector-5ykjaaunx-my-team70.vercel.app](https://heart-disease-detector-5ykjaaunx-my-team70.vercel.app)
- **Description:** Hosted frontend interface for interacting with the heart disease predictor.

## Requirements
The API requires the following dependencies:
- Python 3.x
- FastAPI
- Pydantic
- joblib
- pymongo
- numpy
- scikit-learn==1.2.2

Install them using:
```bash
pip install -r requirements.txt
```



# Text Animation Script

This Python script allows you to add animated text to a video file. It utilizes the `moviepy` library to edit videos and `os` module to handle file paths and directory changes.

## How It Works

The script takes a video file and a list of text entries as input. Each text entry consists of the text to be displayed and its duration in seconds. It then generates a new video file with the specified text animated onto the original video.

1. **Text Entry Specification**: Each text entry in the `text_entries` list is defined by a `TextEntry` object, which includes the text content and its duration.

2. **Text Animation**: The script uses the `TextClip` class from the `moviepy.editor` module to create a text clip for each entry. The text clip is configured with the specified text, fontsize, color, position, and duration.

3. **Video Processing**: The original video file is loaded using `VideoFileClip` class. The text clips are then composited onto the video using the `CompositeVideoClip` class to create the final video with animated text.

4. **Output**: The script saves the resulting video file (`output_video.mp4`) in the current directory.

## Usage

1. Install the required libraries:
   - pydantic
   - List
   - moviepy
2. To run the script, simply do - python animate.py or python3 animate.py


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

