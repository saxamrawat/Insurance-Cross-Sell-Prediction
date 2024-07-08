import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, 
                 gender: str, 
                 age: int, 
                 driving_license: int, 
                 region_code: int, 
                 previously_insured: int, 
                 vehicle_age: str, 
                 vehicle_damage: int, 
                 annual_premium: float, 
                 policy_sales_channel: int, 
                 vintage: int):
        self.gender = gender
        self.age = age
        self.driving_license = driving_license
        self.region_code = region_code
        self.previously_insured = previously_insured
        self.vehicle_age = vehicle_age
        self.vehicle_damage = vehicle_damage
        self.annual_premium = annual_premium
        self.policy_sales_channel = policy_sales_channel
        self.vintage = vintage

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Gender": [self.gender],
                "Age": [self.age],
                "Driving_License": [self.driving_license],
                "Region_Code": [self.region_code],
                "Previously_Insured": [self.previously_insured],
                "Vehicle_Age": [self.vehicle_age],
                "Vehicle_Damage": [self.vehicle_damage],
                "Annual_Premium": [self.annual_premium],
                "Policy_Sales_Channel": [self.policy_sales_channel],
                "Vintage": [self.vintage],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)