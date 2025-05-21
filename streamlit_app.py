
# #...............................................................................................................................................................


# import streamlit as st
# import pandas as pd
# import random
# from datetime import datetime
# import plotly.express as px

# # Streamlit page config
# st.set_page_config(page_title="Device Monitor", layout="wide")
# st.title("📡 Network Device Status Dashboard")

# # Button to manually refresh
# if st.button("🔄 Refresh Data"):
#     st.experimental_rerun()

# # Show current time
# st.markdown(f"🕒 **Current Time:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")

# # Function to generate device data
# def generate_devices():
#     total_devices = 20
#     online_count = int(total_devices * 0.8)

#     devices = []
#     for i in range(1, total_devices + 1):
#         status = "ONLINE" if i <= online_count else "OFFLINE"
#         location = random.choice([
#             "ATC Block", "CNS Block", "Server Room", "Main Gate", "HR",
#             "Radar Room", "Terminal Gate 1", "Director Room", "IT Incharge Room",
#             "Fire Block", "Equipment Room", "Security Room"
#         ])
#         devices.append({
#             "Device Name": f"Device {i}",
#             "IP Address": f"192.168.1.{i}",
#             "Location": location,
#             "Status": status,
#             "Last Checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         })

#     return pd.DataFrame(devices)

# # Get the generated devices
# df_devices = generate_devices()



# # Metrics
# col1, col2 = st.columns(2)
# col1.metric("✅ Online Devices", df_devices[df_devices["Status"] == "ONLINE"].shape[0])
# col2.metric("❌ Offline Devices", df_devices[df_devices["Status"] == "OFFLINE"].shape[0])

# # Pie chart
# st.markdown("### 📊 Device Status Distribution")
# status_count = df_devices["Status"].value_counts().reset_index()
# status_count.columns = ["Status", "Count"]
# fig = px.pie(status_count, names="Status", values="Count", color="Status",
#              color_discrete_map={"ONLINE": "green", "OFFLINE": "red"})
# st.plotly_chart(fig, use_container_width=True)

# # Status coloring
# def highlight_status(val):
#     return f"color: {'green' if val == 'ONLINE' else 'red'}; font-weight: bold"

# st.markdown("### 🧾 Device Table")
# st.dataframe(df_devices.style.applymap(highlight_status, subset=["Status"]), use_container_width=True)

# # CSV download
# csv = df_devices.to_csv(index=False).encode("utf-8")
# st.download_button(
#     label="⬇️ Download Device Status (CSV)",
#     data=csv,
#     file_name="device_status.csv",
#     mime="text/csv"
# )


# #..................................................................................................................................

# # import streamlit as st
# # import pandas as pd
# # import random
# # from datetime import datetime
# # import plotly.express as px

# # # Page config
# # st.set_page_config(page_title="Device Monitor", layout="wide")

# # # Auto-refresh every 30 seconds
# # st.markdown("""
# #     <script>
# #         setTimeout(function(){
# #            window.location.reload();
# #         }, 30000); // 30 seconds
# #     </script>
# # """, unsafe_allow_html=True)

# # st.title("📡 Network Device Status Dashboard")

# # # Display current time
# # st.markdown(f"🕒 **Current Time:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")

# # # Generate device data
# # def generate_devices():
# #     total_devices = 20
# #     online_count = int(total_devices * 0.8)

# #     devices = []
# #     for i in range(1, total_devices + 1):
# #         status = "ONLINE" if i <= online_count else "OFFLINE"
# #         location = random.choice([
# #             "ATC Block", "CNS Block", "Server Room", "Main Gate", "HR",
# #             "Radar Room", "Terminal Gate 1", "Director Room", "IT Incharge Room",
# #             "Fire Block", "Equipment Room", "Security Room"
# #         ])
# #         devices.append({
# #             "Device Name": f"Device {i}",
# #             "IP Address": f"192.168.1.{i}",
# #             "Location": location,
# #             "Status": status,
# #             "Last Checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #         })

# #     return pd.DataFrame(devices)

# # # Load device data
# # df_devices = generate_devices()

# # # Sidebar filters
# # st.sidebar.header("🔍 Filter Devices")
# # locations = ["All"] + sorted(df_devices["Location"].unique().tolist())
# # status_options = ["All", "ONLINE", "OFFLINE"]

# # selected_location = st.sidebar.selectbox("📍 Location", locations)
# # selected_status = st.sidebar.selectbox("⚙️ Status", status_options)

# # if selected_location != "All":
# #     df_devices = df_devices[df_devices["Location"] == selected_location]

# # if selected_status != "All":
# #     df_devices = df_devices[df_devices["Status"] == selected_status]

# # # Metrics
# # col1, col2 = st.columns(2)
# # col1.metric("✅ Online Devices", df_devices[df_devices["Status"] == "ONLINE"].shape[0])
# # col2.metric("❌ Offline Devices", df_devices[df_devices["Status"] == "OFFLINE"].shape[0])

# # # Pie chart
# # st.markdown("### 📊 Device Status Distribution")
# # status_count = df_devices["Status"].value_counts().reset_index()
# # status_count.columns = ["Status", "Count"]
# # fig = px.pie(status_count, names="Status", values="Count", color="Status",
# #              color_discrete_map={"ONLINE": "green", "OFFLINE": "red"})
# # st.plotly_chart(fig, use_container_width=True)

# # # Device table with styled status
# # def highlight_status(val):
# #     return f"color: {'green' if val == 'ONLINE' else 'red'}; font-weight: bold"

# # st.markdown("### 🧾 Device Table")
# # st.dataframe(df_devices.style.applymap(highlight_status, subset=["Status"]), use_container_width=True)

# # # CSV download
# # csv = df_devices.to_csv(index=False).encode("utf-8")
# # st.download_button(
# #     label="⬇️ Download Device Status (CSV)",
# #     data=csv,
# #     file_name="device_status.csv",
# #     mime="text/csv"
# # )

import streamlit as st
import pandas as pd
import pydeck as pdk
import random
from datetime import datetime
import plotly.express as px
import time

# ----------------------------------------------------------------------------------------------------
# Streamlit page configuration
st.set_page_config(page_title="AAI Monitoring Dashboard", layout="wide")

# ----------------------------------------------------------------------------------------------------
# Section 1: Network Device Status Dashboard
st.title("📡 Network Device Status Dashboard")

# Button to manually refresh
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()

# Show current time
st.markdown(f"🕒 **Current Time:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")

# Function to generate device data
def generate_devices():
    total_devices = 20
    online_count = int(total_devices * 0.8)

    devices = []
    for i in range(1, total_devices + 1):
        status = "ONLINE" if i <= online_count else "OFFLINE"
        location = random.choice([
            "ATC Block", "CNS Block", "Server Room", "Main Gate", "HR",
            "Radar Room", "Terminal Gate 1", "Director Room", "IT Incharge Room",
            "Fire Block", "Equipment Room", "Security Room"
        ])
        devices.append({
            "Device Name": f"Device {i}",
            "IP Address": f"192.168.1.{i}",
            "Location": location,
            "Status": status,
            "Last Checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return pd.DataFrame(devices)

# Load device data
df_devices = generate_devices()

# Sidebar filters
st.sidebar.header("🔍 Filter Devices")
locations = ["All"] + sorted(df_devices["Location"].unique().tolist())
status_options = ["All", "ONLINE", "OFFLINE"]

selected_location = st.sidebar.selectbox("📍 Location", locations)
selected_status = st.sidebar.selectbox("⚙️ Status", status_options)

if selected_location != "All":
    df_devices = df_devices[df_devices["Location"] == selected_location]

if selected_status != "All":
    df_devices = df_devices[df_devices["Status"] == selected_status]

# Show data table with styled status
def color_status(val):
    return f"color: {'green' if val == 'ONLINE' else 'red'}; font-weight: bold"

st.subheader("📋 Device Status Table")
st.dataframe(
    df_devices.style.applymap(color_status, subset=["Status"]),
    use_container_width=True
)

# Pie chart of online vs offline
st.subheader("📊 Device Status Overview")
status_counts = df_devices["Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

fig = px.pie(
    status_counts,
    names="Status",
    values="Count",
    color="Status",
    color_discrete_map={"ONLINE": "green", "OFFLINE": "red"},
    title="Online vs Offline Devices"
)
st.plotly_chart(fig, use_container_width=True)

# CSV download
csv = df_devices.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Device Status (CSV)",
    data=csv,
    file_name="device_status.csv",
    mime="text/csv"
)

# Divider between sections
st.divider()

# ----------------------------------------------------------------------------------------------------
# Section 2: AAI Banaras Airport - Server Location Tracker

st.title("🛰️ AAI Banaras Airport - Server Location Tracker")

st.markdown("""
This dashboard shows server placements at **Banaras Airport** with real-time interaction.

**Map Legend:**
- 🟢 Active Servers  
- 🔴 Inactive Servers  
- 🟡 Under Maintenance  
- ✈️ Airport Location
""")

# ---------- Initial Server Data ----------
if 'server_data' not in st.session_state:
    st.session_state.server_data = pd.DataFrame({
        'Server Name': ['Server 1', 'Server 2', 'Server 3', 'Server 4', 'Server 5'],
        'latitude': [25.4522, 25.4530, 25.4510, 25.4538, 25.4546],
        'longitude': [82.8598, 82.8610, 82.8585, 82.8605, 82.8622],
        'Status': ['Active', 'Active', 'Inactive', 'Active', 'Inactive']
    })

server_data = st.session_state.server_data

# ---------- Icon Mapping ----------
def get_icon_url(status):
    return {
        'Active': "https://cdn-icons-png.flaticon.com/512/190/190411.png",       # Green
        'Inactive': "https://cdn-icons-png.flaticon.com/512/1828/1828665.png",    # Red
        'Maintenance': "https://cdn-icons-png.flaticon.com/512/595/595067.png"    # Yellow
    }.get(status, "")

server_data["icon_data"] = server_data["Status"].apply(lambda status: {
    "url": get_icon_url(status),
    "width": 512,
    "height": 512,
    "anchorY": 512
})

# ---------- Airport Location ----------
aai_location = pd.DataFrame({
    'name': ['AAI Banaras Airport'],
    'lat': [25.4520],
    'lon': [82.8590],
    'icon_data': [{
        "url": "https://cdn-icons-png.flaticon.com/512/723/723749.png",
        "width": 512,
        "height": 512,
        "anchorY": 512
    }]
})

# ---------- Pydeck Layers ----------
airport_layer = pdk.Layer(
    "IconLayer",
    data=aai_location,
    get_icon="icon_data",
    get_size=4,
    size_scale=10,
    get_position='[lon, lat]',
    pickable=True
)

server_icon_layer = pdk.Layer(
    "IconLayer",
    data=server_data,
    get_icon="icon_data",
    get_size=4,
    size_scale=8,
    get_position='[longitude, latitude]',
    pickable=True
)

view_state = pdk.ViewState(
    latitude=25.4525,
    longitude=82.8600,
    zoom=16,
    pitch=30
)

st.pydeck_chart(pdk.Deck(
    layers=[airport_layer, server_icon_layer],
    initial_view_state=view_state,
    tooltip={"text": "📡 {Server Name}\nStatus: {Status}"}
))

# ---------- Server Management Form ----------
st.markdown("### ➕ Add / 🗑️ Remove / 🖊️ Update Server")

with st.form("server_form", clear_on_submit=True):
    server_name = st.text_input("Server Name")
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    status = st.selectbox("Status", ['Active', 'Inactive', 'Maintenance'])
    action = st.radio("Action", ["Add", "Update", "Remove"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        if action == "Add":
            if server_name in server_data['Server Name'].values:
                st.warning(f"Server '{server_name}' already exists.")
            else:
                new_row = pd.DataFrame({
                    'Server Name': [server_name],
                    'latitude': [latitude],
                    'longitude': [longitude],
                    'Status': [status],
                    'icon_data': [{
                        "url": get_icon_url(status),
                        "width": 512,
                        "height": 512,
                        "anchorY": 512
                    }]
                })
                st.session_state.server_data = pd.concat([server_data, new_row], ignore_index=True)
                st.success(f"Added '{server_name}' successfully.")

        elif action == "Update":
            index = server_data[server_data['Server Name'] == server_name].index
            if not index.empty:
                st.session_state.server_data.loc[index[0], ['latitude', 'longitude', 'Status']] = [latitude, longitude, status]
                st.session_state.server_data.at[index[0], 'icon_data'] = {
                    "url": get_icon_url(status),
                    "width": 512,
                    "height": 512,
                    "anchorY": 512
                }
                st.success(f"Updated '{server_name}' successfully.")
            else:
                st.warning(f"Server '{server_name}' not found.")

        elif action == "Remove":
            index = server_data[server_data['Server Name'] == server_name].index
            if not index.empty:
                st.session_state.server_data = server_data.drop(index)
                st.success(f"Removed '{server_name}' successfully.")
            else:
                st.warning(f"Server '{server_name}' not found.")

# ---------- Styled Server Table ----------
st.markdown("### 📋 Server Status Table")

def format_status(status):
    return {
        'Active': "🟢 Active",
        'Inactive': "🔴 Inactive",
        'Maintenance': "🟡 Maintenance"
    }.get(status, status)

display_table = st.session_state.server_data.copy()
display_table['Status'] = display_table['Status'].apply(format_status)
display_table = display_table[['Server Name', 'latitude', 'longitude', 'Status']]

st.write(
    display_table.style.set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'center'), ('background-color', '#f0f2f6')]},
        {'selector': 'td', 'props': [('text-align', 'center')]}
    ]).hide(axis='index'),
    unsafe_allow_html=True
)
