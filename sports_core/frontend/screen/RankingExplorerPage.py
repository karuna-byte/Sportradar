import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def ranking_explorer_page():
    st.title("🏆 Rankings Table")

    st.markdown("<br>", unsafe_allow_html=True)

    team_data_model = TeamAnalysisViewModel()
    ranking_data = team_data_model.get_ranking_info()
    df = pd.DataFrame(ranking_data)
    df.index = df.index + 1

    # Sidebar filters
    season = st.sidebar.selectbox(
        "Filter by Season", ["All"] + sorted(df["Season"].dropna().unique())
    )
    week = st.sidebar.selectbox(
        "Filter by Week", ["All"] + sorted(df["Week"].dropna().unique())
    )

    # Rank range slider
    min_rank = int(df["Ranking"].min())
    max_rank = int(df["Ranking"].max())
    rank_range = st.sidebar.slider(
        "Filter by Rank Range", min_rank, max_rank, (min_rank, max_rank)
    )

    # Search box for team name
    search_text = st.text_input("Search by team name")

    # Apply filters
    filtered_df = df.copy()
    if season != "All":
        filtered_df = filtered_df[filtered_df["Season"] == season]
    if week != "All":
        filtered_df = filtered_df[filtered_df["Week"] == week]
    if search_text:
        filtered_df = filtered_df[
            filtered_df["TeamName"].str.contains(search_text, case=False, na=False)
        ]
    # Filter by rank range
    filtered_df = filtered_df[
        (filtered_df["Ranking"] >= rank_range[0])
        & (filtered_df["Ranking"] <= rank_range[1])
    ]

    st.dataframe(
        filtered_df[
            [
                "TeamName",
                "Season",
                "PollName",
                "Week",
                "Ranking",
                "PreviousRanking",
                "Points",
                "FP_Votes",
                "Wins",
                "Losses",
                "Ties",
            ]
        ]
    )
