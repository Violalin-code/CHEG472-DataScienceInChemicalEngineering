#Question 4
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate CSTR volume
def cstr_volume(k, F, X):
    return F / k * (X / (1 - X))

# Function to calculate PFR volume
def pfr_volume(k, F, X):
    return F / k * np.log(1 / (1 - X))

# Streamlit app
def main():
    st.title("Comparison of CSTR and PFR Volumes for First-Order Reactions")

    # User inputs
    k = st.slider("Rate Constant (k)", 0.01, 1.0, 0.1)
    F = st.slider("Flow Rate (F, m^3/s)", 0.1, 10.0, 1.0)
    X_target = st.slider("Target Conversion (X)", 0.01, 0.99, 0.8)

    # Calculate volumes
    V_cstr = cstr_volume(k, F, X_target)
    V_pfr = pfr_volume(k, F, X_target)

    # Display results
    st.write(f"### CSTR Volume: {V_cstr:.2f} m³")
    st.write(f"### PFR Volume: {V_pfr:.2f} m³")

    # Plot volume comparison
    X_vals = np.linspace(0.01, 0.99, 100)
    V_cstr_vals = cstr_volume(k, F, X_vals)
    V_pfr_vals = pfr_volume(k, F, X_vals)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(X_vals, V_cstr_vals, label='CSTR Volume', color='red')
    ax.plot(X_vals, V_pfr_vals, label='PFR Volume', color='blue')
    ax.set_xlabel('Conversion (X)')
    ax.set_ylabel('Volume (m³)')
    ax.set_title('CSTR vs PFR Volume Comparison')
    ax.grid(True)
    ax.legend()

    # Show the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
