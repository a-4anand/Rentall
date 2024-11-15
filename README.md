# RenAll

**RenAll** is a Flask web application that predicts rental prices for residential properties based on various features such as locality, city, area, number of bedrooms (BHK), bathrooms, balconies, and furnishing status. The app uses a pre-trained machine learning model pipeline to provide accurate predictions of rental prices.

## Features

- Predict rental prices based on property characteristics
- User-friendly interface with a form for entering property details
- Flask-based web application
- Real-time prediction using a pre-trained machine learning model pipeline

## Getting Started

### Prerequisites

To run this application locally, you’ll need:
- Python 3.x
- Flask
- joblib
- pandas

Ensure these dependencies are installed.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/RenAll.git
   cd RenAll
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Model File:

Ensure that the pre-trained model pipeline file (rent_prediction_model_pipeline.pkl) is placed in the project root directory.
The model should include preprocessing steps to handle the input features provided by the form.
Run the Application:

bash
Copy code
python app.py
The application will run on http://127.0.0.1:5000 by default.

Usage
Open the application by navigating to http://127.0.0.1:5000 in your browser.
Enter the following details about the property:
Locality
City
Area (in square feet)
BHK (number of bedrooms)
Bathrooms
Balconies
Furnishing status (e.g., fully furnished, semi-furnished)
Submit the form to get the predicted rental price for the property.
The result will display the predicted rent on the same page with the format: Predicted Rent: ₹<amount>.
File Structure
bash
Copy code
RenAll/
│
├── app.py                       # Main application file
├── rent_prediction_model_pipeline.pkl  # Pre-trained model pipeline
├── templates/
│   └── index.html               # Main HTML file for the user interface
├── requirements.txt             # Dependencies for the project
└── README.md                    # Project README file
Model and Pipeline
The application uses a pre-trained machine learning model pipeline (rent_prediction_model_pipeline.pkl) loaded via joblib. This pipeline includes all preprocessing steps necessary to handle the form inputs. A placeholder value of 0 is used for the feature area_rate.

Pipeline Steps: Ensure that the pipeline includes transformations for the following input features:
locality
city
area
bhk
bathrooms
balconies
furnishing
Error Handling
In case of any errors during prediction (e.g., missing or invalid inputs), an error message will be displayed:

javascript
Copy code
Error during prediction: <error message>
This message will help identify any issues, such as missing model files or incorrect data formats.

Contributing
If you'd like to contribute to RenAll, please fork the repository and create a pull request. Contributions to improve the model, enhance the interface, or fix bugs are welcome!

License
This project is open source and available under the MIT License.

yaml
Copy code

---

This is now a properly formatted **README.md** file. You can copy and paste this into your project repository's README file.





