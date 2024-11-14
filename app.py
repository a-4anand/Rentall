from flask import Flask, request, render_template
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the pre-trained model pipeline, which should include preprocessing steps
pipeline = joblib.load('rent_prediction_model_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form inputs (without area_rate)
        locality = request.form['locality']
        city = request.form['city']
        area = float(request.form['area'])
        bhk = int(request.form['bhk'])
        bathrooms = int(request.form['bathrooms'])
        balconies = int(request.form['balconies'])
        furnishing = request.form['furnishing']

        # Prepare the input data, with a placeholder for 'area_rate'
        input_data = pd.DataFrame([[locality, city, area, bhk, bathrooms, balconies, furnishing, 0]],  # Placeholder 0 for area_rate
                                  columns=['locality', 'city', 'area', 'bhk', 'bathrooms', 'balconies', 'furnishing', 'area_rate'])

        # Apply the preprocessing pipeline and make the prediction
        prediction = pipeline.predict(input_data)[0]

        return render_template('index.html', prediction_text=f"Predicted Rent: ₹{prediction:.2f}")

    except Exception as e:
        return f"Error during prediction: {e}"




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
