# Diabetes Prediction Web Application

## Overview
The **Diabetes Prediction Web Application** is a user-friendly and AI-powered tool designed to assess an individual's risk of diabetes based on their health indicators and lifestyle factors. Using a machine learning model trained on a large dataset from the CDC's BRFSS2015 survey, this application predicts whether a user is diabetic, prediabetic, or non-diabetic, providing immediate results and actionable health advice.

## Key Features
- **Accurate Prediction Model:** Powered by a CatBoost model with a 97.21% accuracy rate.
- **User-Friendly Interface:** Built with Django, HTML, and CSS to ensure smooth user experience.
- **Real-Time Data Processing:** Collects user health data, such as blood pressure, cholesterol, BMI, smoking status, and more, to generate predictions instantly.
- **Big Data Integration:** Utilizes a dataset of 253,681 survey responses with 21 key features.
- **Health Insights:** Offers tailored advice based on the user's diabetic risk level.
- **Scalable and Secure:** Designed with Django's robust backend, ensuring scalability and data security.

## Technology Stack
- **Backend:** Django
- **Frontend:** HTML, CSS
- **Model Training:** Python (Pandas, NumPy, Scikit-Learn, CatBoost)
- **Dataset:** CDC's BRFSS2015 survey data

## Project Goals
- **Early Detection:** Help users identify their diabetes risk early and encourage proactive health management.
- **User Empowerment:** Provide personalized insights to motivate lifestyle changes.
- **Healthcare Support:** Assist healthcare providers by identifying at-risk individuals.
- **Data-Driven Insights:** Leverage big data and machine learning to enhance predictive accuracy.

## How to Run the Project
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the project directory:**
   ```bash
   cd diabetes-prediction-webapp
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the Django server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

Stay healthy and proactive — **Diabetes Prediction Web Application** is here to guide you on your health journey.

