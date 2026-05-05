# Churn-Prediction
Customer Churn Prediction is a machine learning web app that predicts whether a customer will leave a service based on customer data. Built with Python, Scikit-learn, and Streamlit, it helps businesses improve retention through accurate churn analysis.


Customer Churn Prediction System
📌 Project Overview

The Customer Churn Prediction System is a Machine Learning web application designed to predict whether a customer is likely to discontinue using a company’s service.

This project helps businesses:

Identify potential churn customers
Improve customer retention strategies
Make data-driven decisions
Reduce revenue loss

The application uses customer demographic and service-related information to predict churn status through a trained machine learning model.

🚀 Features
User-friendly Streamlit Web App
Real-time churn prediction
Clean data preprocessing pipeline
Feature engineering for improved accuracy
Multiple classification models tested
Hyperparameter tuning
Model serialization using Pickle
Interactive prediction results
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle
Matplotlib / Seaborn


📂 Project Structure
Customer-Churn-Prediction/
│
├── app.py                 # Streamlit application
├── churn_model.pkl        # Trained machine learning model
├── requirements.txt       # Required libraries
├── README.md              # Project documentation
└── dataset.csv            # Customer churn dataset



📊 Dataset Information

The dataset includes customer attributes such as:

Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Internet Service
Online Security
Contract Type
Payment Method
Monthly Charges
Total Charges
Target Variable:
Churn
1 → Customer Churned
0 → Customer Retained

⚙️ Data Preprocessing Steps
Handling missing values
Encoding categorical variables
Feature scaling
Train-test split
Feature selection
Pipeline integration
🤖 Machine Learning Models Used

Some commonly tested models:

Logistic Regression
Random Forest Classifier
Decision Tree
XGBoost
Support Vector Machine
Final Model Selection:

The best-performing model was selected based on:

Accuracy
Precision
Recall
F1 Score
📈 Model Performance Metrics

Example:

Accuracy: 85%+
Precision: 83%
Recall: 81%
F1 Score: 82%
----------------------------------------------------

🌐 Streamlit Application

The app allows users to:

Input customer details
Click on Predict
View churn prediction instantly
Prediction Output:
Customer Churned
Customer Not Churned


💻 Installation Guide
Clone Repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

Install Dependencies
pip install -r requirements.txt

Run Application
streamlit run app.py

📷 Sample Interface
Customer Data Input Form
Predict Button
Churn Status Display

🔍 Future Enhancements
Deploy on cloud platforms
Add dashboard analytics
Improve model accuracy with deep learning
Bulk customer prediction
Business intelligence reporting

🎯 Use Cases
Telecom industry
Subscription businesses
Banking
SaaS platforms
E-commerce retention analysis

👨‍💻 Author
Sudheer Muthyala
ECE Graduate | Full Stack Developer | Machine Learning Enthusiast

📜 License
This project is for educational and portfolio purposes.

⭐ Conclusion
This project demonstrates:
End-to-end ML pipeline development
Data preprocessing expertise
Classification model implementation
Web deployment using Streamlit
Real-world business problem solving

The Customer Churn Prediction System is a practical solution for reducing customer loss and improving retention strategies.











