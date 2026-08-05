import joblib
import pandas as pd

# Load the trained model
model = joblib.load("telecom_tower_model.pkl")

# New tower data for prediction
new_data = pd.DataFrame({
    "Tower_ID": [11],
    "Temperature_C": [55],
    "Battery_Voltage": [48.5],
    "Power_Consumption_W": [2800],
    "Signal_Strength_Percent": [65],
    "Fan_Speed_RPM": [3000],
    "Humidity_Percent": [70],
    "Traffic_Load": [2500],
    "Tower_Age_Years": [5]
})

# Predict
prediction = model.predict(new_data)

# Display result
if prediction[0] == 1:
    print("Hardware Failure Predicted within 48 Hours")
else:
    print("Tower is Healthy")
