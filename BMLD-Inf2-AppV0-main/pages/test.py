import streamlit as st

st.title("💧 Dichte-Rechner für Flüssigkeiten")

with st.form("density_form"):
    st.header("🔢 Berechnung der Dichte")
    
    # Eingabe von Masse und Volumen
    mass = st.number_input("Masse (in kg)", min_value=0.0, format="%.2f")
    volume = st.number_input("Volumen (in m³)", min_value=0.0, format="%.4f")
    
    # Berechnung starten
    calculate = st.form_submit_button("Berechnen")
    
    if calculate:
        if volume > 0:
            density = mass / volume
            st.success(f"Die berechnete Dichte beträgt: {density:.2f} kg/m³")
        else:
            st.error("Das Volumen muss größer als 0 sein!")

 