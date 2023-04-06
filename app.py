import streamlit as st

from modules.stability_check import stability_check
from utils.plotter import plot_wall
from utils.session import get_session_state

session_state = get_session_state(height=2.0, top_breadth=0.3, base_breadth=0.7, Ka=0.3, gamma_soil=20.0, gamma_stone=22.0, surcharge=10.0, water_table=0.0, passive_soil_height=0.0, Kp=2.0 )

st.title("Stone Retaining Wall Stability Check")

height = st.number_input("Height (m)", min_value=0.0, value=session_state['height'])
top_breadth = st.number_input("Top Breadth (m)", min_value=0.0, value=session_state['top_breadth'])
base_breadth = st.number_input("Base Breadth (m)", min_value=0.0, value=session_state['base_breadth'])
Ka = st.number_input("Coefficient of active earth pressure, Ka", min_value=0.0, value=session_state['Ka'])
gamma_soil = st.number_input("Gamma Soil (kN/m³)", min_value=0.0, value=session_state['gamma_soil'])
gamma_stone = st.number_input("Gamma Stone (kN/m³)", min_value=0.0, value=session_state['gamma_stone'])
surcharge = st.number_input("Surcharge (kN/m²)", min_value=0.0, value=session_state['surcharge'])
water_table = st.number_input("Water Height (m)", min_value=0.0, value=session_state['water_table'])

st.subheader("Passive Soil")
passive_soil_height = st.number_input("Height of passive soil (m)", min_value=0.0, max_value=100.0, value=session_state['passive_soil_height'], step=0.1)
Kp = st.number_input("Coefficient of passive earth pressure, Kp", min_value=0.0, max_value=10.0, value=session_state['Kp'], step=0.1)

get_session_state(height=height, top_breadth=top_breadth, base_breadth=base_breadth, Ka=Ka, gamma_soil=gamma_soil, gamma_stone=gamma_stone, surcharge=surcharge, water_table=water_table, passive_soil_height=passive_soil_height, Kp=Kp)

# if st.button("Calculate Stability"):
stability_factor_overturning, stability_factor_sliding, weight, active_soil_pressure, passive_soil_pressure, lateral_surcharge, lateral_water, base_friction_force = stability_check(height, top_breadth, base_breadth, Ka, Kp,gamma_soil, gamma_stone, passive_soil_height, surcharge, water_table)

# Stability results
st.write("## Stability Check Results")

if stability_factor_overturning >= 2:
    st.markdown(f"<p style='color: green;'><b>Overturning Safety Factor: {stability_factor_overturning:.2f} (OK)</b></p>", unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color: red;'><b>Overturning Safety Factor: {stability_factor_overturning:.2f} (NOT OK)</b></p>", unsafe_allow_html=True)

if stability_factor_sliding >= 1.5:
    st.markdown(f"<p style='color: green;'><b>Sliding Safety Factor: {stability_factor_sliding:.2f} (OK)</b></p>", unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color: red;'><b>Sliding Safety Factor: {stability_factor_sliding:.2f} (NOT OK)</b></p>", unsafe_allow_html=True)

    fig = plot_wall(height, top_breadth, base_breadth, weight, active_soil_pressure, passive_soil_pressure, passive_soil_height, lateral_surcharge, water_table, lateral_water, base_friction_force)
    st.pyplot(fig)

# Save the user inputs in session state
session_state['height'] = height
session_state['top_breadth'] = top_breadth
session_state['base_breadth'] = base_breadth
session_state['Ka'] = Ka
session_state['gamma_soil'] = gamma_soil
session_state['gamma_stone'] = gamma_stone
session_state['surcharge'] = surcharge
session_state['water_table'] = water_table
session_state['passive_soil_height'] = passive_soil_height
session_state['Kp'] = Kp