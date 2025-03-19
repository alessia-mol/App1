from utils import helpers
import streamlit as st

def berechne_dichte(mass, volume, timezone='Europe/Zurich'):      
     if volume > 0:
      density = mass / volume
      st.success(f"✅ Die berechnete Dichte beträgt: {density:.2f} kg/m³")
     else:
        st.error("⚠️ Das Volumen muss größer als 0 sein!")

     result_dict = {
        "timestamp": helpers.ch_now(),
        "Masse": mass,
        "Volumen": volume,
        "Dichte": density,} 

     return result_dict