import streamlit as st
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel
import pandas as pd


def players_explorer_page():
    st.title("👥 Players Explorer")

    st.markdown("<br>", unsafe_allow_html=True)

    team_data_model = TeamAnalysisViewModel()
    player_data = team_data_model.get_all_players_info()
    df = pd.DataFrame(player_data)
    df.index = df.index + 1

    # Sidebar filters
    position = st.sidebar.selectbox(
        "Filter by Position", ["All"] + sorted(df["Position"].dropna().unique())
    )
    status = st.sidebar.selectbox(
        "Filter by Status", ["All"] + sorted(df["Status"].dropna().unique())
    )
    eligibility = st.sidebar.selectbox(
        "Filter by Eligibility", ["All"] + sorted(df["Eligibility"].dropna().unique())
    )

    # Search box for player first name or team name
    search_text = st.text_input("Search by player first name or team name")

    # Apply filters
    filtered_df = df.copy()
    if position != "All":
        filtered_df = filtered_df[filtered_df["Position"] == position]
    if status != "All":
        filtered_df = filtered_df[filtered_df["Status"] == status]
    if eligibility != "All":
        filtered_df = filtered_df[filtered_df["Eligibility"] == eligibility]
    if search_text:
        filtered_df = filtered_df[
            filtered_df["TeamName"].str.contains(search_text, case=False, na=False)
            | filtered_df["PalyerFirstName"].str.contains(
                search_text, case=False, na=False
            )
        ]

    st.dataframe(
        filtered_df[
            [
                "TeamName",
                "PalyerFirstName",
                "PlayerLastName",
                "AbbreviationName",
                "BirthPlace",
                "Position",
                "Height",
                "Weight",
                "Status",
                "Eligibility",
            ]
        ]
    )
