import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def home_page():
    st.title("🏠 Home Dashboard")
    st.write("Welcome to NCAAFB")

    st.markdown(
        "<div style='padding:10px; background:#eef; border-radius:8px;'>Experience a fully connected analytics system that brings together rankings, teams, players, and game data into one relationally linked ecosystem. Gain deeper insights, track performance trends, and unlock advanced decision-making through a powerful, centralized data platform built for NCAA Football analysis.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style='padding:10px; font-weight:700; background-color:#f0f0f5; color: #8B0000; border-radius:6px;'>
        Available Teams
    </div>
    """,
        unsafe_allow_html=True,
    )

    team_data_model = TeamAnalysisViewModel()
    team_data = team_data_model.get_all_team_info()
    df = pd.DataFrame(team_data)
    df.index = df.index + 1
    st.dataframe(
        df[
            [
                "MarketName",
                "TeamName",
                "TeamNameAlias",
                "ConferenceName",
            ]
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style='padding:10px; font-weight:700; background-color:#f0f0f5; color: #8B0000; border-radius:6px;'>
        Players Information
    </div>
    """,
        unsafe_allow_html=True,
    )

    team_data_model = TeamAnalysisViewModel()
    player_data = team_data_model.get_all_players_info()
    df = pd.DataFrame(player_data)
    df.index = df.index + 1
    st.dataframe(
        df[
            [
                "PalyerFirstName",
                "PlayerLastName",
                "AbbreviationName",
                "TeamName",
            ]
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div style='padding:10px; font-weight:700; background-color:#f0f0f5; color: #8B0000; border-radius:6px;'>
        Season Information
    </div>
    """,
        unsafe_allow_html=True,
    )

    team_data_model = TeamAnalysisViewModel()
    season_data = team_data_model.get_season_info()
    df = pd.DataFrame(season_data)
    df.index = df.index + 1
    st.dataframe(
        df[
            [
                "SeasonYear",
                "StartDate",
                "EndDate",
                "Status",
            ]
        ]
    )
