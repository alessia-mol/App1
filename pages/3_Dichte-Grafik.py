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

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['Masse'], 
                use_container_width=True)
st.caption('Masse über Zeit (kg)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['Volumen'],
                use_container_width=True)
st.caption('Volumen über Zeit (m³)')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['Dichte'],
                use_container_width=True)
st.caption('Dichte über Zeit')