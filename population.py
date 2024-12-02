import numpy as np
import streamlit as st
import joblib

# Load model
model = joblib.load("population_predictor_model.joblib")  # Ensure the model file is correct

st.title('Population Predictor')

# Get user input
City = st.text_input('City')
Country = st.text_input('Country')
Population_2023 = st.text_input('Population_2023')
Growth_Rate = st.text_input('Growth_Rate (%)')

# Debugging: Display input values
st.write(f"Population_2023 entered: {Population_2023}")
st.write(f"Growth_Rate entered: {Growth_Rate}")

# Make prediction
if st.button('Predict'):
    try:
        # Validate and clean inputs
        if not Population_2023 or not Growth_Rate:
            raise ValueError("Population_2023 and Growth Rate are required.")

        # Convert inputs to float
        pop_cleaned = float(Population_2023)
        growth_rate_cleaned = float(Growth_Rate.replace('%', '').strip())

        # Prepare input data
        input_data = np.array([[pop_cleaned, growth_rate_cleaned]])
        prediction = model.predict(input_data)

        # Display prediction
        st.write(f"Predicted population for {Country} {City} in 2024 is: {prediction[0]:,.2f}")

    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
