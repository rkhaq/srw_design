import streamlit as st

from modules.stability_check import stability_check
from utils.plotter import plot_wall

st.title("Stone Retaining Wall Stability Check")

height = st.number_input("Height (m)", min_value=0.0, value=1.0)
top_breadth = st.number_input("Top Breadth (m)", min_value=0.0, value=0.3)
base_breadth = st.number_input("Base Breadth (m)", min_value=0.0, value=0.7)
Ka = st.number_input("Coefficient of active earth pressure, Ka", min_value=0.0, value=0.3)
gamma_soil = st.number_input("Gamma Soil (kN/m³)", min_value=0.0, value=20.0)
gamma_stone = st.number_input("Gamma Stone (kN/m³)", min_value=0.0, value=22.0)
surcharge = st.number_input("Surcharge (kN/m²)", min_value=0.0, value=10.0)
water_table = st.number_input("Water Height (m)", min_value=0.0)

st.subheader("Passive Soil")
passive_soil_height = st.number_input("Height of passive soil (m)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
Kp = st.number_input("Coefficient of passive earth pressure, Kp", min_value=0.0, max_value=10.0, value=2.0, step=0.1)


if st.button("Calculate Stability"):
    stability_factor_overturning, stability_factor_sliding, weight, active_soil_pressure, passive_soil_pressure, lateral_surcharge, lateral_water = stability_check(height, top_breadth, base_breadth, Ka, Kp,gamma_soil, gamma_stone, passive_soil_height, surcharge, water_table)
    st.write(f"Stability Factor for Overturning: {stability_factor_overturning:.2f}")
    st.write(f"Stability Factor for Sliding: {stability_factor_sliding:.2f}")
    st.write(f"Weight of the wall: {weight:.2f} kN/m")
    st.write(f"Active Soil Pressure: {active_soil_pressure:.2f} kN/m")
    st.write(f"Passive Soil Pressure: {passive_soil_pressure:.2f} kN/m")

    fig = plot_wall(height, top_breadth, base_breadth, weight, active_soil_pressure, passive_soil_pressure, passive_soil_height, lateral_surcharge, water_table, lateral_water)
    st.pyplot(fig)