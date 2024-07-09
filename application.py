from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

## Route for home page
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            age=int(request.form.get('age')),
            driving_license=int(request.form.get('driving_license')),
            region_code=int(request.form.get('region_code')),
            previously_insured=int(request.form.get('previously_insured')),
            vehicle_age=request.form.get('vehicle_age'),
            vehicle_damage=request.form.get('vehicle_damage'),
            annual_premium=float(request.form.get('annual_premium')),
            policy_sales_channel=int(request.form.get('policy_sales_channel')),
            vintage=int(request.form.get('vintage'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        return render_template('home.html', results=results[0])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
