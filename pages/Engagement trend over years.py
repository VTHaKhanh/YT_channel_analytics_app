import streamlit as st
import pandas as pd
import plotly.express as px
# streamlit run

# Retrieve df from session state
if "df" in st.session_state:
    df = st.session_state["df"]
else:
    st.write("No dataset found. Please load it on the main page.")
# __________________________________________________________________________________________________________________________________

# --- line chart ---

# --- KPI Trend Over Time ---
st.subheader("2. Nr of Views, Likes, Comments Over Year", divider="violet")

st.markdown("""
### Key Metrics Over the Years
The main figures of a YouTube channel include:  
- **Number of Views (`view_count`)**  
- **Number of Likes (`likes_count`)**  
- **Number of Comments (`comments_count`)**  

Below are the aggregated figures by year.
""")

# Aggregate data: Sum view count by Published Year
kpis_by_year = df.groupby("Published Year")[["view_count", "like_count", "comment_count"]].sum().reset_index()

# Convert numeric columns to space-separated format
kpis_by_year["view_count"] = kpis_by_year["view_count"].apply(lambda x: f"{x:,}".replace(",", " "))
kpis_by_year["like_count"] = kpis_by_year["like_count"].apply(lambda x: f"{x:,}".replace(",", " "))
kpis_by_year["comment_count"] = kpis_by_year["comment_count"].apply(lambda x: f"{x:,}".replace(",", " "))

# Show table and format Published Year value
st.dataframe(kpis_by_year)

st.markdown("""
Overall, the trends of these three engagement metrics are closely related.
""")

# 1. View chart
# Create the trend line using Plotly
fig_view_count = px.line(
    kpis_by_year, 
    x="Published Year", 
    y="view_count", 
    markers=True
)

# Fix the X-axis to treat "Published Year" as a categorical variable
fig_view_count.update_layout(
    xaxis=dict(type="category"),  # Forces X-axis to be categorical
    xaxis_fixedrange=True,   # Disables zoom & pan on the X-axis
    yaxis_fixedrange=True,   # Disables zoom & pan on the Y-axis
    modebar_remove=['zoom', 'pan', 'autoscale', 'resetScale', 'select', 'fullscreen'] # Removes toolbar buttons
)

st.plotly_chart(fig_view_count)

# 2. Like chart
# Create the trend line using Plotly
fig_like_count = px.line(
    kpis_by_year, 
    x="Published Year", 
    y="like_count", 
    markers=True
)

# Fix the X-axis to treat "Published Year" as a categorical variable
fig_like_count.update_layout(
    xaxis=dict(type="category"),  # Forces X-axis to be categorical
    xaxis_fixedrange=True,   # Disables zoom & pan on the X-axis
    yaxis_fixedrange=True,   # Disables zoom & pan on the Y-axis
    modebar_remove=['zoom', 'pan', 'autoscale', 'resetScale', 'select', 'fullscreen'] # Removes toolbar buttons
)

st.plotly_chart(fig_like_count)

# 3. Comment chart
# Create the trend line using Plotly
fig_comment_count = px.line(
    kpis_by_year, 
    x="Published Year", 
    y="comment_count", 
    markers=True
)

# Fix the X-axis to treat "Published Year" as a categorical variable
fig_comment_count.update_layout(
    xaxis=dict(type="category"),  # Forces X-axis to be categorical
    xaxis_fixedrange=True,   # Disables zoom & pan on the X-axis
    yaxis_fixedrange=True,   # Disables zoom & pan on the Y-axis
    modebar_remove=['zoom', 'pan', 'autoscale', 'resetScale', 'select', 'fullscreen'] # Removes toolbar buttons
)

st.plotly_chart(fig_comment_count)


