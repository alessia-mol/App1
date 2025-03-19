# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st

st.title('Dichte Verlauf')

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Dichte Daten vorhanden. Berechnen Sie die Dichte auf der Startseite.')
    st.stop()

# Masse über Zeit
st.subheader('Masse über Zeit (kg)')
st.line_chart(data=data_df.set_index('timestamp')['Masse'], 
                use_container_width=True)

# Volumen über Zeit
st.subheader('Volumen über Zeit (m³)')
st.line_chart(data=data_df.set_index('timestamp')['Volumen'],
                use_container_width=True)

# Dichte über Zeit
st.subheader('Dichte über Zeit (kg/m³)')
st.line_chart(data=data_df.set_index('timestamp')['Dichte'],
                use_container_width=True)