import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def coaches_explorer_page():
    st.title("🧑‍🏫 Coaches Explorer")

    st.markdown("<br>", unsafe_allow_html=True)

    team_data_model = TeamAnalysisViewModel()
    coaches_data = team_data_model.get_coach_info()
    df = pd.DataFrame(coaches_data)
    df.index = df.index + 1

    # Search box for coach name or team
    search_text = st.text_input("Search by coach name or team")

    # Apply filters
    filtered_df = df.copy()
    if search_text:
        filtered_df = filtered_df[
            filtered_df["TeamName"].str.contains(search_text, case=False, na=False)
            | filtered_df["CoachName"].str.contains(search_text, case=False, na=False)
        ]

    st.dataframe(
        filtered_df[
            [
                "TeamName",
                "CoachName",
                "Position",
            ]
        ]
    )
