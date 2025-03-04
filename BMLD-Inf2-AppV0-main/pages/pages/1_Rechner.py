import streamlit as st
from utils import helpers  # Importiere die Funktion aus helpers.py

def rechner_page():
    st.title("Penetrationszeit-Rechner")
    st.write("Berechnung der Zeit basierend auf der Formel t = (d / K)²")
    st.write("Autoren: Max Mustermann, Erika Musterfrau")
    st.write("E-Mails: max@example.com, erika@example.com")
    
    # Erklärung der Formel
    with st.expander("Erklärung der Formel"):
        st.write("Die Formel t = (d / K)² beschreibt den Zusammenhang zwischen Eindringtiefe, einer Materialkonstanten K und der benötigten Zeit.")
    
    # Formular für Benutzereingaben
    with st.form("penetration_time_form"):
        d = st.number_input("Eindringtiefe d (m)", min_value=0.0, format="%.4f")
        K = st.slider("K-Wert", min_value=0.0001, max_value=10.0, value=1.0, step=0.0001)
        
        submitted = st.form_submit_button("Berechnen")
        
        if submitted:
            result = helpers.berechne_zeit(d, K)
            st.write(f"Ergebnis: {result['message']}")
            if result["time"] is not None:
                st.write(f"Die benötigte Zeit beträgt: {result['time']} s")
            st.write(f"Berechnet am: {result['timestamp'].strftime('%d.%m.%Y %H:%M:%S')}")

# Diese Funktion wird aufgerufen, wenn die Seite in Streamlit geöffnet wird
if __name__ == "__main__":
    rechner_page()
    

    
