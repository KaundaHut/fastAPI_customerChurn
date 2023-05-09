### Customer Churn Prediction API with FastAPI
#### This repository contains an API for predicting customer churn using FastAPI. The API is built with Python 3.8 and uses a machine learning model trained on customer data to make predictions.
### Getting Started
#### 1 Install the required packages: pip install -r requirements.txt
#### 2 Run the server: uvicorn app.main:app --reload
### Project Structure
#### The project has the following structure:
#### ├── app
#### │   ├── main.py
#### │   ├── svm_clf.pp
#### │   └── procfile.py
#### ├── .gitignore
#### ├── README.md
#### ├── Runtime.txt
#### app: Contains the main application code, including the FastAPI app (main.py), the machine learning model (svm_clf.py), and procfile.py is a mechanism for declaring what commands are run by application's containers on the Deis platform.
#### README.md: This file!
#### Runtime.txt: Code that implements portions of a programming language's execution model.
### Contributing
#### If you would like to contribute to the project, feel free to submit a pull request or open an issue. Any feedback or suggestions are welcome!


