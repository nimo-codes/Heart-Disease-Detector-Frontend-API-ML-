# Heart Disease Predictor

## Overview
Heart Disease Predictor is a web application that predicts the likelihood of heart disease based on various input parameters. It includes a FastAPI backend for making predictions and a frontend interface for user interaction. try it? : URL: https://heart-disease-detector-5ykjaaunx-my-team70.vercel.app

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
- scikit-learn=1.2.2

Install them using:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

