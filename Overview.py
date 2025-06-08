import streamlit as st
import pandas as pd

# streamlit run

# Sidebar for navigation
# st.sidebar.page_link("pages/Engagement trend over years.py", label="Go to Second Page")
# st.sidebar.page_link("pages/page_3.py", label="Go to Third Page")

# __________________________________________________________________________________________________________________________________

# --- Load Data ---

# Streamlit caching decorator
# If the function load_data() is called multiple times, it won’t reload the dataset each time but fetch the cached result
@st.cache_data
def load_data():
    # data file in the same directory
    df = pd.read_csv("YT_data_ext.csv")  

    # Convert to datetime format
    df['published_at'] = pd.to_datetime(df['published_at'])

    # Convert duration to total seconds
    df['duration_seconds'] = df['duration'].apply(lambda x: pd.Timedelta(x).total_seconds())

    # Add additional date-related columns
    df['Published Month Year'] = df['published_at'].dt.strftime('%Y%m')  # YYYYMM (e.g., 202502)
    df['Published Year'] = df['published_at'].dt.year.astype(int)
    df['Published Date'] = df['published_at'].dt.strftime('%Y%m%d')  # YYYYMMDD (e.g., 20250225)
    df['Published Date2'] = df['published_at'].dt.strftime('%Y%m%d')  # YYYYMMDD (e.g., 20250225)
    df['Published Time'] = df['published_at'].dt.strftime('%H:%M')  # HH:MM (e.g., 06:54)


    # Sort data by Published Date DESC and Published Time DESC
    df = df.sort_values(by=['Published Date', 'Published Time'], ascending=[False, False])

    # Calculate "Days from previous video"
    df['Published Date2'] = pd.to_datetime(df['Published Date2'], format='%Y%m%d')
    df['Days from previous video'] = df['Published Date2'].diff(-1).dt.days

    # Drop unnecessary columns
    df = df.drop(columns=['published_at', 'channel_title', 'duration','Published Date2'])

    return df

st.header("Youtube Channel Data Analysis", divider="violet")
st.subheader("1. Published video data | All dataset | No filter applied", divider="violet")

st.markdown("""
### Data Source  
The dataset was extracted from a public YouTube channel using Google Cloud YouTube Data API on **30.5.2025**.  

The dataset includes key attributes of videos such as **titles, descriptions, dates, views, and different engagement metrics**.  

#### Steps:  
- Create and configure YouTube API  
- Run extraction script locally  
- Store CSV locally  
""")

df = load_data()

# Show table and format Published Year value - for plotting in engagement trend page
st.dataframe(df.style.format({"Published Year": "{:.0f}"}))

# Convert Published Year to string format - for plotting in engagement trend page
df["Published Year"] = df["Published Year"].astype(str)

# Store df in Streamlit's session state
st.session_state["df"] = df  