from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your saved model
with open("xgb_model_pickle.pkl", "rb") as file:
    model = pickle.load(file)

def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        vals = [
            float(request.form['PM2.5']),
            float(request.form['PM10']),
            float(request.form['NO']),
            float(request.form['NO2']),
            float(request.form['NOx']),
            float(request.form['NH3']),
            float(request.form['CO']),
            float(request.form['SO2']),
            float(request.form['O3']),
            float(request.form['Benzene']),
            float(request.form['Toluene']),
            float(request.form['Xylene'])
        ]

        # Predict AQI
        pred = model.predict(np.array(vals).reshape(1, -1))[0]
        category = aqi_category(pred)

        return render_template('index.html', prediction_text=f"AQI = {pred:.2f} → {category}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)

