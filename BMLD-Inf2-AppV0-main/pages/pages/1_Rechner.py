import streamlit as st
from utils import helpers  # Importiere die Funktion aus helpers.py

def main():
    st.title("Penetrationszeit-Rechner")
    st.write("Berechnung der Zeit basierend auf der Formel t = (d / K)²")
    st.write("Autoren: Max Mustermann, Erika Musterfrau")
    st.write("E-Mails: max@example.com, erika@example.com")
    
    # Erklärung der Formel in einem Expander
    with st.expander("Erklärung der Formel"):
        st.write("Die Formel t = (d / K)² beschreibt den Zusammenhang zwischen Eindringtiefe, einer Materialkonstanten K und der benötigten Zeit.")
    
    # Formular für Benutzereingaben
    with st.form("penetration_time_form"):
        # Benutzer gibt die Eindringtiefe und den K-Wert ein
        d = st.number_input("Eindringtiefe d (m)", min_value=0.0, format="%.4f")
        K = st.slider("K-Wert", min_value=0.0001, max_value=10.0, value=1.0, step=0.0001)
        
        # Formular absenden
        submitted = st.form_submit_button("Berechnen")
        
        if submitted:
            # Berechnung der Zeit
            result = helpers.berechne_zeit(d, K)  # Verwende die Funktion aus helpers.py
            
            # Ergebnisse anzeigen
            st.write(f"Ergebnis: {result['message']}")
            if result["time"] is not None:
                st.write(f"Die benötigte Zeit beträgt: {result['time']} s")
            st.write(f"Berechnet am: {result['timestamp'].strftime('%d.%m.%Y %H:%M:%S')}")

if __name__ == "__main__":
    main()
    
    
