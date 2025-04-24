import streamlit as st
import folium
from streamlit_folium import folium_static
from datetime import datetime
import time
import random

# Import dataset and functions
from dataset import get_sample_data, get_coordinates

# Load sample data
crime_data = get_sample_data()
# Initialize crime data in session_state if not already done
if 'crime_data' not in st.session_state:
    st.session_state.crime_data = get_sample_data()

# Use session-managed data throughout the app
crime_data = st.session_state.crime_data

# ----------------------------
# 🌑 Dark Theme & Styling
st.set_page_config(page_title="Crime Watch - Code Pulse", layout="wide")
st.markdown("""
    <style>
    body, .main {
        background-color: #1e1e1e;
        color: white;
        font-family: "Segoe UI", sans-serif;
    }
    h1, h2, h3 {
        color: #ff9800;
    }
    .report-box {
        background-color: #333333;
        padding: 10px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🚨 Header
st.title("🚨 Crime Watch (Tamil Nadu)")
st.markdown("#### 🔍 Real-time Detection & Reporting by Team **Code Pulse**")

# ----------------------------
# Filter and View Existing Reports
if st.button("📊 Load Crime Reports"):
    with st.spinner("Fetching latest crime reports..."):
        time.sleep(1.5)
        st.success("✅ Crime data loaded!")

    city_names = ["All"] + sorted(set(report['text'].split()[-1] for report in crime_data))
    selected = st.selectbox("🗺️ Filter by City:", city_names)

    filtered = crime_data if selected == "All" else [c for c in crime_data if selected in c['text']]

    st.subheader("📝 Crime Records")
    for c in filtered:
        st.markdown(f"<div class='report-box'>🕒 {c['time']}<br>📌 {c['text']}</div>", unsafe_allow_html=True)

    m = folium.Map(location=[10.8505, 76.2711], zoom_start=7)
    for c in filtered:
        folium.Marker([c['lat'], c['lon']], popup=f"{c['text']} ({c['time']})", icon=folium.Icon(color='red')).add_to(m)
    st.subheader("📍 Crime Map")
    folium_static(m)

# ----------------------------
# Report a Crime (New Features)
st.subheader("🚨 Add a New Crime Report")

with st.form("report_form"):
    new_report = st.text_area("📄 Describe the incident:")
    city_input = st.text_input("🏙️ Enter city name (Tamil Nadu only):")
    action = st.form_submit_button("🧾 Submit")

    if action and new_report and city_input:
        coords = get_coordinates(city_input)
        if coords:
            lat, lon = coords
        else:
            # Random fallback within Tamil Nadu
            lat, lon = random.uniform(8.0, 13.5), random.uniform(76.0, 80.5)

        new_entry = {
            "text": f"{new_report} ({city_input.strip().title()})",
            "lat": lat,
            "lon": lon,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        crime_data.append(new_entry)
        st.success("✅ Crime reported and added to the map!")
        st.markdown(f"<div class='report-box'>🆕 {new_entry['time']}<br>📌 {new_entry['text']}</div>", unsafe_allow_html=True)

# ----------------------------
# Footer
st.markdown("---")
st.markdown("<center><small>Team <b>Code Pulse</b> | Real-time Crime Tracker 🇮🇳</small></center>", unsafe_allow_html=True)
