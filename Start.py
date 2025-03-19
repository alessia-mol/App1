import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App1")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp'])

import streamlit as st
import pandas as pd

st.title("Dichte-Rechner für Feststoffe")

st.markdown("""
### ℹ️ Über den Dichte-Rechner

Der **Dichte-Rechner für Feststoffe** ist ein benutzerfreundliches Tool zur Berechnung der Dichte eines Materials anhand von Masse und Volumen.  
Die Dichte wird in **kg/m³** angegeben und hilft, Materialien wie **Metalle, Holz oder Gesteine** zu vergleichen.

🔹 **So funktioniert es:**  
Geben Sie einfach die **Masse (kg)** und das **Volumen (m³)** ein, und das Tool berechnet die Dichte automatisch.  
Zusätzlich werden Beispielwerte für Materialien wie **Eis, Gold und Kiefer** angezeigt, um den berechneten Wert einzuordnen.
""")


# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Noëlle Keel (keelnoe1@students.zhaw.ch)
- Alessia Molignini (moligale@students.zhaw.ch)


"""