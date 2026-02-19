# Student-Productivity-Sleep-Analysis
Machine Learning project to analyze student sleep behaviour and productivity using Python and Streamlit.
## About
This project is based on a simple idea:  
As a student, I observed that daily habits like study time, screen usage, sleep hours and physical activity directly affect productivity and sleep quality.

So I created this Machine Learning project to analyze and predict:

- Sleep Quality Score  
- Productivity Score  

based on daily lifestyle data.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Streamlit  

---

## Project Workflow

1. Collected student daily habit data in Excel.
2. Loaded and analyzed data using Pandas.
3. Trained Linear Regression models.
4. Saved models using Pickle.
5. Built a Streamlit web app for prediction.

---

## How to Run the Project

Install dependencies:
pip install -r reqirement.txt

Run the application:
straemlit run analyzer_app.py

---

## Features

- Predicts sleep quality
- Predicts productivity score
- Gives performance category (Low / Moderate / High)
- Provides simple improvement suggestions

---

This project helped me understand:
- Data preprocessing
- Model training
- Model deployment
- Basic web app development using Streamlit
  
---

## Project Structure

Student-Productivity-Sleep-Analysis/
│
├── analyzer_app.py          # Streamlit application file
├── model.ipynb              # Model training notebook
├── sleep_model.pkl          # Trained sleep prediction model
├── productivity_model.pkl   # Trained productivity pridiction model
├── student_data.xlsx        # Dataset file used for training
├── requirements.txt         # Required python libraries
└── Project Report.pdf       # Internship project report
---
## Application Preview

## Application Preview

<p align="center">
  <img src="app_screenshot_input.png" width="650"/>
  <img src="app_screenshot_output.png" width="650"/>
</p>


