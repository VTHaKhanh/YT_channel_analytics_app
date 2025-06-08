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

# --- Sidebar Filters --- Not dynamic

st.sidebar.title("Filters")

# Store Published Year selection
selected_year = st.sidebar.selectbox("Select Published Year:", ["All"] + sorted(df["Published Year"].unique(), reverse=True))

# For plotting in engagement page, published year type was changed to str, now change to int to calculate YoY values
df["Published Year"] = df["Published Year"].astype(int)

# last_year is calculated when a specific year is selected
last_year = selected_year - 1 if selected_year != "All" else selected_year


# Store Published Month Year selection
selected_month_year = st.sidebar.selectbox("Select Published Month Year:", ["All"] + sorted(df["Published Month Year"].unique(), reverse=True))

# Store Published Date selection
selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + sorted(df["Published Date"].unique(), reverse=True))

# Store Published Time selection
selected_time = st.sidebar.selectbox("Select Published Time:", ["All"] + sorted(df["Published Time"].unique()))


# --- Sidebar Filters --- Dynamic

# # Define the available years
# selected_year = st.sidebar.selectbox("Select Published Year:", ["All"] + sorted(df["Published Year"].unique(), reverse=True))
# last_year = selected_year - 1 if selected_year != "All" else selected_year


# # Define available month-year values based on selected year
# if selected_year != "All":
#     selected_month_year = st.sidebar.selectbox("Select Published Month Year:", ["All"] + sorted(df[df["Published Year"] == selected_year]["Published Month Year"].unique(), reverse=True))
# else:
#     selected_month_year = st.sidebar.selectbox("Select Published Month Year:", ["All"] + sorted(df["Published Month Year"].unique(), reverse=True))


# Define available dates based on selected month-year
# if selected_year == "All" and selected_month_year == "All":
#     selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + sorted(df["Published Date"].unique(), reverse=True))
# if selected_year != "All" and selected_month_year != "All":
#     selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + sorted(df[df["Published Month Year"] == selected_month_year]["Published Date"].unique(), reverse=True))
# if selected_year == "All" and selected_month_year != "All":
#     selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + sorted(df[df["Published Month Year"] == selected_month_year]["Published Date"].unique(), reverse=True))
# if selected_year != "All" and selected_month_year == "All":
#     selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + sorted(df[df["Published Year"] == selected_year]["Published Date"].unique(), reverse=True))


# Define available times based on selected date
# if selected_date != "All":
#     selected_time = sorted(df[df["Published Date"] == selected_date]["Published Time"].unique())
# else:
#     selected_time = sorted(df["Published Time"].unique())

# Store selections with dynamically updated options
# selected_year = st.sidebar.selectbox("Select Published Year:", ["All"] + available_years)
# selected_month_year = st.sidebar.selectbox("Select Published Month Year:", ["All"] + available_months)
# selected_date = st.sidebar.selectbox("Select Published Date:", ["All"] + available_dates)
# selected_time = st.sidebar.selectbox("Select Published Time:", ["All"] + available_times)

# __________________________________________________________________________________________________________________________________

# --- Apply Filters to df2, create df2_prev as previous year in accordance with df2 ---
# Define df2
df2 = df

if selected_year != "All":
    df2 = df[df["Published Year"] == selected_year]

if selected_month_year != "All":
    df2 = df[df["Published Month Year"] == selected_month_year]

if selected_date != "All":
    df2 = df[df["Published Date"] == selected_date]

if selected_time != "All":
    df2 = df[df["Published Time"] == selected_time]

# Define df2_prev - which is previous year in accordance with selection of df2 - df_prev is for YoY calculation, no need to show df2_prev
df2_LY = df

if selected_year != "All":
    df2_LY = df[df["Published Year"] == last_year]

# --- Filtered Data ---

# Define the preferred column order
preferred_order = ["Published Year", "Published Month Year", "Published Date", "Days from previous video", "Published Time", 
                   "view_count", "like_count", "comment_count", "duration_seconds"]

# Identify remaining columns that are not in the preferred order
remaining_columns = [col for col in df.columns if col not in preferred_order]

# Reorder df2
df2 = df2[preferred_order + remaining_columns]

# __________________________________________________________________________________________________________________________________

# --- KPIs scorecard for filtered df2 and previous year df2_prev ---

st.subheader("3. Key Performance Indicators", divider="violet")

st.markdown("""
### Metrics to Consider  
Besides the three main engagement KPIs, it's worth evaluating:  
1️ | **Performance of each video** _(Per Vid-related figures)_  
2️ | **Uploading frequency** _(Time between two videos)_  

These metrics can be calculated from the original dataset.
""")

st.markdown("""
### Yearly Comparison  
Filter a specific year to compare **Year-over-Year (YoY) changes** in the scorecard.
""")

# Calculate distinct count of video_id
nr_of_vid_during_selected_time_period = df2["video_id"].nunique()

# videos uploaded in the time period selected
st.write(f"**There are {nr_of_vid_during_selected_time_period} videos published in the time period selected.**")


# Calculate stats for df2
avg_views, min_views, max_views, total_views = df2["view_count"].mean(), df2["view_count"].min(), df2["view_count"].max(), df2["view_count"].sum()

avg_likes, min_likes, max_likes, total_likes = df2["like_count"].mean(), df2["like_count"].min(), df2["like_count"].max(), df2["like_count"].sum()

avg_comments, min_comments, max_comments, total_comments  = df2["comment_count"].mean(), df2["comment_count"].min(), df2["comment_count"].max(), df2["comment_count"].sum()

avg_duration, min_duration, max_duration = df2["duration_seconds"].mean(), df2["duration_seconds"].min(), df2["duration_seconds"].max()

avg_days_from_prev_vid, min_days_from_prev_vid, max_days_from_prev_vid = df2["Days from previous video"].mean(), df2["Days from previous video"].min(), df2["Days from previous video"].max()


# Calculate stats for df2_LY
avg_views_LY, min_views_LY, max_views_LY, total_views_LY = df2_LY["view_count"].mean(), df2_LY["view_count"].min(), df2_LY["view_count"].max(), df2_LY["view_count"].sum()

avg_likes_LY, min_likes_LY, max_likes_LY, total_likes_LY = df2_LY["like_count"].mean(), df2_LY["like_count"].min(), df2_LY["like_count"].max(), df2_LY["like_count"].sum()

avg_comments_LY, min_comments_LY, max_comments_LY, total_comments_LY = df2_LY["comment_count"].mean(), df2_LY["comment_count"].min(), df2_LY["comment_count"].max(), df2_LY["comment_count"].sum()

avg_duration_LY, min_duration_LY, max_duration_LY = df2_LY["duration_seconds"].mean(), df2_LY["duration_seconds"].min(), df2_LY["duration_seconds"].max()

avg_days_from_prev_vid_LY, min_days_from_prev_vid_LY, max_days_from_prev_vid_LY = df2_LY["Days from previous video"].mean(), df2_LY["Days from previous video"].min(), df2_LY["Days from previous video"].max()


# Calculate YoY %


# --- Calculate Year-over-Year (YoY) Change ---
avg_views_YoY_change = ((avg_views - avg_views_LY) / avg_views_LY) * 100
min_views_YoY_change = ((min_views - min_views_LY) / min_views_LY) * 100
max_views_YoY_change = ((max_views - max_views_LY) / max_views_LY) * 100
total_views_YoY_change = ((total_views - total_views_LY) / total_views_LY) * 100

avg_likes_YoY_change = ((avg_likes - avg_likes_LY) / avg_likes_LY) * 100
min_likes_YoY_change = ((min_likes - min_likes_LY) / min_likes_LY) * 100
max_likes_YoY_change = ((max_likes - max_likes_LY) / max_likes_LY) * 100
total_likes_YoY_change = ((total_likes - total_likes_LY) / total_likes_LY) * 100

avg_comments_YoY_change = ((avg_comments - avg_comments_LY) / avg_comments_LY) * 100
min_comments_YoY_change = ((min_comments - min_comments_LY) / min_comments_LY) * 100
max_comments_YoY_change = ((max_comments - max_comments_LY) / max_comments_LY) * 100
total_comments_YoY_change = ((total_comments - total_comments_LY) / total_comments_LY) * 100

avg_duration_YoY_change = ((avg_duration - avg_duration_LY) / avg_duration_LY) * 100
min_duration_YoY_change = ((min_duration - min_duration_LY) / min_duration_LY) * 100
max_duration_YoY_change = ((max_duration - max_duration_LY) / max_duration_LY) * 100

avg_days_from_prev_vid_YoY_change = ((avg_days_from_prev_vid - avg_days_from_prev_vid_LY) / avg_days_from_prev_vid_LY) * 100
min_days_from_prev_vid_YoY_change = ((min_days_from_prev_vid - min_days_from_prev_vid_LY) / min_days_from_prev_vid_LY) * 100 if min_days_from_prev_vid_LY != 0 else 0
max_days_from_prev_vid_YoY_change = ((max_days_from_prev_vid - max_days_from_prev_vid_LY) / max_days_from_prev_vid_LY) * 100


# Create KPI columns 

# YoY (delta values) changes are showed only when 1 year value is selected
# Condition: Show YoY change only when no filters are applied
show_condition_YoY = (
    selected_month_year == "All" and
    selected_date == "All" and
    selected_time == "All" and
    selected_year != "All"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Views", value=f"{total_views:,}", delta=f"{total_views_YoY_change:.1f}%" if show_condition_YoY else None)

    st.metric(label="📊 Avg Views Per Vid", value=f"{avg_views:,.0f}", delta=f"{avg_views_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="❤️ Avg Likes Per Vid", value=f"{avg_likes:,.0f}", delta=f"{avg_likes_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="💬 Avg Comments Per Vid", value=f"{avg_comments:,.0f}", delta=f"{avg_comments_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="⏳ Avg Duration (sec) Per Vid", value=f"{avg_duration:,.1f}", delta=f"{avg_duration_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Avg days between 2 videos", value=f"{avg_days_from_prev_vid:,.1f}", delta=f"{avg_days_from_prev_vid_YoY_change:.1f}%" if show_condition_YoY else None)

with col2:
    st.metric(label="Total Likes", value=f"{total_likes:,}", delta=f"{total_likes_YoY_change:.1f}%" if show_condition_YoY else None)

    st.metric(label="Min Views", value=f"{min_views:,}", delta=f"{min_views_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Min Likes", value=f"{min_likes:,}", delta=f"{min_likes_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Min Comments", value=f"{min_comments:,}", delta=f"{min_comments_YoY_change:.1f}%" if show_condition_YoY else None)

    # Ensure delta is displayed only if YoY condition is met
    delta_min_duration = f"{min_duration_YoY_change:.1f}%" if show_condition_YoY and min_duration_YoY_change != 0 else None
    delta_min_days = f"{min_days_from_prev_vid_YoY_change:.1f}%" if show_condition_YoY and min_days_from_prev_vid_YoY_change != 0 else None

    st.metric(label="Min Duration (sec)", value=f"{min_duration:,.1f}", delta=delta_min_duration)
    st.metric(label="Min days between 2 videos", value=f"{min_days_from_prev_vid:,.1f}", delta=delta_min_days)

with col3:
    st.metric(label="Total Comments", value=f"{total_comments:,}", delta=f"{total_comments_YoY_change:.1f}%" if show_condition_YoY else None)

    st.metric(label="Max Views", value=f"{max_views:,}", delta=f"{max_views_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Max Likes", value=f"{max_likes:,}", delta=f"{max_likes_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Max Comments", value=f"{max_comments:,}", delta=f"{max_comments_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Max Duration (sec)", value=f"{max_duration:,.1f}", delta=f"{max_duration_YoY_change:.1f}%" if show_condition_YoY else None)
    st.metric(label="Max days between 2 videos", value=f"{max_days_from_prev_vid:,.1f}", delta=f"{max_days_from_prev_vid_YoY_change:.1f}%" if show_condition_YoY else None)


st.markdown("""  
Below is the filtered dataset for your own exploration""")

# Filtered data
st.dataframe(df2)

# __________________________________________________________________________________________________________________________________
















