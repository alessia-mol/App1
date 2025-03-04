import streamlit as st
 
def calculate_t(d, K):

    try:

        t = (d / K) ** 2

        return t

    except ZeroDivisionError:

        return "Fehler: K darf nicht null sein!"
 
st.title("Rechner für die Formel (t = (d/K)^2)")
 
d = st.number_input("Wert für d eingeben:", value=1.0, step=0.1)

K = st.number_input("Wert für K eingeben:", value=1.0, step=0.1)
 
if st.button("Berechnen"):

    result = calculate_t(d, K)

    st.write(f"Ergebnis: {result}")

 