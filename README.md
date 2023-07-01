# Read me⚠ 
## Greetings 💐

# Aadhar Card Details Verification System

This project is a Flask application that takes input from a form (name, Aadhar number, and roll number), verifies the details against a MongoDB database, and displays the verified candidate details on a web page.

## Prerequisites

Make sure you have the following software and packages installed before running the application:

- UiPath Studio: [Download](https://www.uipath.com/start-trial)
- Python 3: [Download](https://www.python.org/downloads/)
- Flask: Install using `pip install flask`
- pymongo: Install using `pip install pymongo`
- openpyxl: Install using `pip install openpyxl`

## Installation

1. Clone or download the project repository.
2. Make Sure You Have install:
```
Flask==2.0.1
pymongo==3.12.0
openpyxl==3.0.7
```
3. Make sure you have MongoDB installed and running on your local machine.

## Usage

1. Open the `Display.py` file and update the MongoDB connection details (`host` and `port`) as per your configuration.
2. Run the following command to start the Flask server.
3. 3. Access the application in your web browser at `http://localhost:5000`.
4. Fill in the form fields (name, Aadhar number, and roll number) and submit the form.
5. The application will verify the provided details against the MongoDB database.
6. If the details are found in the database, the verified candidate details will be displayed on the web page.
7. If the details are not found or the verification fails, an appropriate message will be displayed.


## Screenshots

Here are some screenshots of the application pages:

# 1. Home Page:
  ![Screenshot (17)](https://github.com/jaisuriya97/RPA-Uipath/assets/80122325/a5387f83-88c4-4a46-846a-f8f4d015201e)

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


## Thank You ☠
