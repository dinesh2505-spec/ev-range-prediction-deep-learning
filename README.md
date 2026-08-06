🚗 **EV Range Prediction using Deep Learning**

A production-ready end-to-end Machine Learning project that predicts the driving range of electric vehicles using an Artificial Neural Network (ANN). This project demonstrates the complete ML lifecycle—from data analysis and model development to API deployment, containerization using Docker, CI/CD automation, and cloud deployment on Google Cloud.  

predictor link: https://ev-range-prediction-28863701301.europe-west3.run.app/

 **📌 Project Overview**
This project develops a Deep Learning model capable of predicting an EV's driving range based on its technical specifications.

Unlike a notebook-only ML project, this repository demonstrates how a machine learning model can be deployed as a production-ready web application using modern MLOps practices.

**🎯 Project Objectives**
. Perform data cleaning and exploratory data analysis (EDA)
. Build a Multiple Linear Regression baseline
. Develop a Deep Learning ANN model using TensorFlow/Keras
. Model Evaluation
. Save and reload trained models
. Deploy the model through a FastAPI REST API
. Containerize the application using Docker
. Automate testing with GitHub Actions (CI)
. Automate cloud deployment using GitHub Actions (CD)
. Deploy the application on Google Cloud Run

**🛠 Tech Stack**
Programming Language
. Python 3.11

Data Science & Machine Learning
. NumPy
. Pandas
. Matplotlib
. Scikit-learn
. TensorFlow / Keras

Web framework
. FastAPI
. Uvicorn
. HTML
. Jinja2 Templates

Containerization
. Docker

Version Control
. Git
. GitHub

CI/CD
. GitHub Actions

Cloud Platform
. Google Cloud Platform (GCP)
. Google Artifact Registry
. Google Cloud Run

**📂 Project Structure**

<img width="456" height="752" alt="image" src="https://github.com/user-attachments/assets/891f0709-5939-4b89-88bc-a906b902774e" />



**📊 Machine Learning Workflow**

1. Data Understanding
    . Dataset exploration
    . Feature inspection
    . Missing value analysis
    . Data cleaning

2. Exploratory Data Analysis
Visualized relationships between EV range and important features including:

    . Battery Capacity
    . Efficiency
    . Torque
    . Acceleration
    . Top Speed
    . Vehicle Dimensions

3. Feature Engineering

Selected numerical features for prediction and prepared the data for training.

4. Model Development

Implemented:

Multiple Linear Regression
Artificial Neural Network (ANN)

The ANN model was developed using TensorFlow/Keras and trained to predict vehicle range.

5. Model Evaluation

The trained model was evaluated using:

       Mean Absolute Error (MAE)
       Training Loss
       Validation Loss

6. Model Persistence

The final model and preprocessing scaler are stored for inference.

models/
├── final_ev_range_ann_model.keras
└── scaler.pkl

**🖥 User Interface**

A clean and interactive web interface has been developed using FastAPI and HTML templates, allowing users to predict the driving range of an electric vehicle directly from their web browser.

The interface is designed to be simple and intuitive so that users without programming knowledge can interact with the trained machine learning model.

**Prediction Workflow**

User 
│ 
▼ 
Open Web Application 
│ 
▼ 
Enter EV Specifications 
│ 
▼ 
Click "Predict" 
│ 
▼ FastAPI API 
│ 
▼ Data Preprocessing 
│ 
▼ TensorFlow ANN Model 
│ 
▼ Predicted EV Range 
│ 
▼ Result Displayed on the Webpage

<img width="726" height="276" alt="image" src="https://github.com/user-attachments/assets/57a4275c-c6fe-4490-8afb-f5e96631e15f" />

**🌐 REST API**

The trained model is also exposed as a REST API using FastAPI, enabling integration with external applications and services.

Home Endpoint
GET /

Returns the web interface.

Prediction Endpoint
POST /predict

Example Input

{
  "battery_capacity_kWh": 77,
  "efficiency_wh_per_km": 165,
  "torque_nm": 600,
  "acceleration_0_100_s": 4.8,
  "top_speed_kmh": 210
}

Example Response

{
  "predicted_range_km": 520.4
}

**🔄 CI/CD Pipeline**

Every push to the main branch automatically:

Runs automated tests using Pytest
Builds a Docker image
Pushes the image to Google Artifact Registry
Deploys the latest application to Google Cloud Run

Authentication is implemented using Google Cloud Workload Identity Federation, eliminating the need for long-lived service account keys and following Google Cloud security best practices.

**Skills Demonstrated**
Machine Learning
  Data Cleaning
  Exploratory Data Analysis
  Feature Engineering
  Multiple Linear Regression
  Artificial Neural Networks
  TensorFlow / Keras
  Model Evaluation
  Model Persistence
  
Software Engineering
    Python Programming
    FastAPI Development
    REST API Design
    HTML Template Integration
    Modular Project Structure
    Git Version Control
MLOps
    Docker
    GitHub Actions
    Continuous Integration
    Continuous Deployment
    Google Artifact Registry
    Google Cloud Run
    Workload Identity Federation
    Production Deployment
    
Cloud Computing
    Google Cloud Platform
    Cloud Run
    Artifact Registry
    Container-based Deployment


**🚀 Future Improvements**
Model versioning
Model monitoring
Cloud Monitoring dashboards
Prediction analytics
Explainable AI (SHAP)
Batch prediction
Kubernetes deployment
AWS deployment using ECR and ECS/Fargate

**👨‍💻 Author**

Dinesh Reddy Male

Functional Safety Engineer transitioning into Machine Learning and MLOps, passionate about building production-ready AI applications using Deep Learning, Cloud Computing, DevOps, and modern software engineering practices.

Feel free to connect with me on LinkedIn.






   
