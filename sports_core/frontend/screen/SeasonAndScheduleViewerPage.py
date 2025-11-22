import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def season_and_schedule_viewer_page():
    st.title("📅 Season & Schedule Viewer")

    st.markdown("<br>", unsafe_allow_html=True)

    team_data_model = TeamAnalysisViewModel()
    season_data = team_data_model.get_season_info()
    df = pd.DataFrame(season_data)
    df.index = df.index + 1

    # Sidebar filters
    seasonYear = st.sidebar.selectbox(
        "Filter by Season Year", ["All"] + sorted(df["SeasonYear"].dropna().unique())
    )
    status = st.sidebar.selectbox(
        "Filter by Status", ["All"] + sorted(df["Status"].dropna().unique())
    )

    # Apply filters
    filtered_df = df.copy()
    if seasonYear != "All":
        filtered_df = filtered_df[filtered_df["SeasonYear"] == seasonYear]
    if status != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status]

    st.dataframe(
        filtered_df[
            [
                "SeasonYear",
                "StartDate",
                "EndDate",
                "Status",
            ]
        ]
    )