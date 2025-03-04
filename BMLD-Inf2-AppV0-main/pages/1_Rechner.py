import streamlit as st
import math
import matplotlib.pyplot as plt

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
        st.write("Die Formel t = (d / K)² beschreibt den Zusammenhang zwischen Eindringtiefe, einer Materialkonstante K und der benötigten Zeit.")
    
    with st.form("penetration_time_form"):
        d = st.number_input("Eindringtiefe d (m)", min_value=0.0, format="%.4f")
        K = st.slider("K-Wert", min_value=0.0001, max_value=10.0, value=1.0, step=0.0001)
        
        submitted = st.form_submit_button("Berechnen")
        
        if submitted:
            t = berechne_zeit(d, K)
            if t is not None:
                st.write(f"Die benötigte Zeit beträgt: {t:.4f} s")
                
                # Plot der Beziehung zwischen d und t
                fig, ax = plt.subplots()
                d_values = [i / 10 for i in range(1, 101)]
                t_values = [(di / K) ** 2 for di in d_values]
                ax.plot(d_values, t_values, label=f"K={K}")
                ax.set_xlabel("Eindringtiefe d (m)")
                ax.set_ylabel("Zeit t (s)")
                ax.set_title("Zusammenhang zwischen d und t")
                ax.legend()
                st.pyplot(fig)
            else:
                st.write("Ungültige Eingabe. K darf nicht 0 sein.")

if __name__ == "__main__":
    main()
    
