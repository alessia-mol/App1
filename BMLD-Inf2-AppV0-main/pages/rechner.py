import streamlit as st
 
def berechne_zeit(d, K):

    if K > 0:

        return (d / K) ** 2

    else:

        return None
 
def main():

    st.title("Penetrationszeit-Rechner")

    st.write("Berechnung der Zeit basierend auf der Formel t = (d / K)²")

    st.write("Autoren: Max Mustermann, Erika Musterfrau")

    st.write("E-Mails: max@example.com, erika@example.com")

    with st.expander("Erklärung der Formel"):

        st.write("Die Formel t = (d / K)² beschreibt den Zusammenhang zwischen Eindringtiefe, einer Materialkonstanten K und der benötigten Zeit.")

    with st.form("penetration_time_form"):

        d = st.number_input("Eindringtiefe d (mm)", min_value=0.0, format="%.4f")

        K = st.slider("K-Wert", min_value=0.0001, max_value=10.0, value=1.0, step=0.0001)

        submitted = st.form_submit_button("Berechnen")

        if submitted:

            t = berechne_zeit(d, K)

            if t is not None:

                st.write(f"Die benötigte Zeit beträgt: {t:.6f} h")

            else:

                st.write("Ungültige Eingabe. K darf nicht 0 sein.")
 
if __name__ == "__main__":

    main()

 
 