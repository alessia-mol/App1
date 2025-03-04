import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Seiten-Layout
st.set_page_config(page_title="Dichte-Rechner für Feststoffe", page_icon="📏", layout="centered")

# Stil-Verbesserung mit Markdown und CSS
st.markdown(
    """
    <style>
    .stApp { background-color: #f5f5f5; }
    .title { text-align: center; color: #8B4513; font-size: 28px; }
    .stTextInput, .stNumberInput, .stButton { border-radius: 10px; }
    .info-box { background-color: #d2b48c; padding: 10px; border-radius: 10px; color: #4b2e2e; }
    .chart-container { text-align: center; }
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
    
    # Berechnung starten
    calculate = st.form_submit_button("🛠️ Berechnen")
    
    if calculate:
        if volume > 0:
            density = mass / volume
            st.success(f"✅ Die berechnete Dichte beträgt: {density:.2f} kg/m³")
            
            # Visualisierung
            fig, ax = plt.subplots()
            materials = ["Aluminium", "Eisen", "Gold", "Kupfer", "Ihr Material"]
            densities = [2700, 7874, 19300, 8960, density]
            colors = ["blue", "gray", "gold", "brown", "red"]
            
            ax.bar(materials, densities, color=colors)
            ax.set_ylabel("Dichte (kg/m³)")
            ax.set_title("Vergleich der Dichte mit bekannten Materialien")
            
            st.pyplot(fig)
        else:
            st.error("⚠️ Das Volumen muss größer als 0 sein!")

# Fun Fact oder Wissenswertes
st.markdown("""
### 🧐 Wussten Sie schon?
- Gold hat eine der höchsten Dichten von Metallen: 19.300 kg/m³.
- Holzarten haben sehr unterschiedliche Dichten – Eiche ist viel dichter als Kiefer.
- Materialien mit hoher Dichte werden oft für Schutzkleidung oder Strahlenschutz verwendet.
""")
