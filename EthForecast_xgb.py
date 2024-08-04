import pandas as pd
import numpy as np
import streamlit as st
import xgboost as xgb
# from xgboost import XGBRegressor
# from sklearn.preprocessing import MinMaxScaler, StandardScaler
# from sklearn.metrics import mean_squared_error, mean_absolute_error


#Loading up the regressor model we created
XGB_tuned = xgb.XGBRegressor()
XGB_tuned.load_model('eth_xgb_model1.json')


#Caching the model for faster loading
#@st.cache



# Function to make predictions
def make_predictions(data):
    
    """
    Note that data for predictions must first be transformed to the the data put in the model to make accurate predictions.
    """
    features = ['Open', 'High', 'Low', 'Total Supply', 'Tokens Transferred USD - Internal', 'Fund Price (USD)', 'Coinbase Premium Gap']

    X_test = data[features].iloc[-1:]
    
    predictions = load_model.predict(X_test)

    return predictions

#=== writing the Predictor App
st.title('Ethereum Close Price Dashboard')
st.image("""https://th.bing.com/th/id/R.59ab41db4afa6cce16b4a707ee6bbbb9?rik=UwFPzZOK0Vp0%2fA&pid=ImgRaw&r=0""")
st.header('Upload your dataset to predict the Ethereum close price:')

# File uploader for the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)
    
    # Show the uploaded data
    st.write("Uploaded Data:")
    st.write(data)
    
    if st.button('Predict Close Price'):
        try:
            # Ensure the data has the correct format
            if 'Datetime' in data.columns:
                data = data.drop(columns=['Datetime'])
            
            
            # Make predictions
            predictions = make_predictions(data)
            
            st.success(f'The predicted close price is ${predictions[0]:.2f}')
        except Exception as e:
            st.error(f"Error: {e}")



