import streamlit as st
# Seiten-Layout
st.set_page_config(page_title="Dichte-Rechner für Feststoffe", page_icon="📏", layout="centered")

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import pandas as pd
from functions.Dichte_calculator import berechne_dichte

st.markdown(
    """
    <style>
    .stApp { background-color: #f5f5f5; }
    .title { text-align: center; color: #8B4513; font-size: 28px; }
    .stTextInput, .stNumberInput, .stButton { border-radius: 10px; }
    .info-box { background-color: #d2b48c; padding: 10px; border-radius: 10px; color: #4b2e2e; }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown("<h1 class='title'>📏 Dichte-Rechner für Feststoffe</h1>", unsafe_allow_html=True)

# Einführungstext
st.markdown("""
<div class='info-box'>
    Die Dichte eines Feststoffs gibt an, wie viel Masse sich in einem bestimmten Volumen befindet. 
    Sie wird in Kilogramm pro Kubikmeter (kg/m³) angegeben und ist eine wichtige Eigenschaft 
    für Materialien wie Metalle, Holz oder Gesteine.
</div>
""", unsafe_allow_html=True)

# Hauptcontainer
with st.form("density_form"):
    st.header("🔢 Berechnung der Dichte")
    
    # Eingabe von Masse und Volumen mit Platzhaltern
    mass = st.number_input("Masse (in kg)", min_value=0.0, format="%.2f", placeholder="Geben Sie die Masse ein")
    volume = st.number_input("Volumen (in m³)", min_value=0.0, format="%.4f", placeholder="Geben Sie das Volumen ein")
    
    # Berechnung 
    calculate = st.form_submit_button("🛠️ Berechnen")
    
    if calculate:
        result = berechne_dichte(mass, volume)
   
        # --- Save Dichte data ---
        from utils.data_manager import DataManager
        DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage 
            
# Vergleichsdaten
materialien = ['Eis', 'Gold', 'Kiefer', 'Berechneter Wert']
werte = [920, 19300, 600]  # Dichte in kg/m³ (Beispieldaten)

# Berechneten Wert hinzufügen
if calculate and volume > 0:
    berechnete_dichte = mass / volume
    werte.append(round(berechnete_dichte, 2))
else:
    werte.append(0)  # Platzhalterwert, falls keine Berechnung erfolgt

# Erstelle DataFrame für Darstellung als Tabelle
df = pd.DataFrame({'Materialien': materialien, 'Dichte (kg/m³)': [round(w, 2) for w in werte]})

# Streamlit App
st.markdown("### Vergleich der Dichten der Materialien")

# Tabelle anzeigen
st.dataframe(df)

st.markdown("""
### 🧐 Wussten Sie schon?
- **Eisberge** schwimmen im Wasser, weil Eis mit ca. 920 kg/m³ eine geringere Dichte als Wasser haben.
- **Gold** hat eine der höchsten Dichten von Metallen: 19'300 kg/m³.
- **Holzarten** haben sehr unterschiedliche Dichten – Eiche ist viel dichter als Kiefer.""")



