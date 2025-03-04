import streamlit as st

# Seiten-Layout
st.set_page_config(page_title="Dichte-Rechner", page_icon="💧", layout="centered")

# Stil-Verbesserung mit Markdown und CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #e6f7ff; }
    .title { text-align: center; color: #0073e6; }
    .stTextInput, .stNumberInput, .stButton { border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Titel
st.markdown("<h1 class='title'>💧 Dichte-Rechner für Flüssigkeiten</h1>", unsafe_allow_html=True)

# Hauptcontainer
with st.form("density_form"):
    st.header("🔢 Berechnung der Dichte")
    
    # Eingabe von Masse und Volumen mit Platzhaltern
    mass = st.number_input("Masse (in kg)", min_value=0.0, format="%.2f", placeholder="Geben Sie die Masse ein")
    volume = st.number_input("Volumen (in m³)", min_value=0.0, format="%.4f", placeholder="Geben Sie das Volumen ein")
    
    # Berechnung starten
    calculate = st.form_submit_button("💡 Berechnen")
    
    if calculate:
        if volume > 0:
            density = mass / volume
            st.success(f"✅ Die berechnete Dichte beträgt: {density:.2f} kg/m³")
        else:
            st.error("⚠️ Das Volumen muss größer als 0 sein!")