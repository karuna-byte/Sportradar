import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def teams_explorer_page():
    st.title("🧩 Teams Explorer")

    team_data_model = TeamAnalysisViewModel()
    team_data = team_data_model.get_all_team_info()
    df = pd.DataFrame(team_data)
    df.index = df.index + 1

    # Sidebar filters
    conference = st.sidebar.selectbox(
        "Filter by Conference", ["All"] + sorted(df["ConferenceName"].dropna().unique())
    )
    division = st.sidebar.selectbox(
        "Filter by Division", ["All"] + sorted(df["DivisionName"].dropna().unique())
    )
    state = st.sidebar.selectbox(
        "Filter by State", ["All"] + sorted(df["VenueState"].dropna().unique())
    )

    # Search box for team name or alias
    search_text = st.text_input("Search for a team by name or alias")

    # Apply filters
    filtered_df = df.copy()
    if conference != "All":
        filtered_df = filtered_df[filtered_df["ConferenceName"] == conference]
    if division != "All":
        filtered_df = filtered_df[filtered_df["DivisionName"] == division]
    if state != "All":
        filtered_df = filtered_df[filtered_df["VenueState"] == state]
    if search_text:
        filtered_df = filtered_df[
            filtered_df["TeamName"].str.contains(search_text, case=False, na=False)
            | filtered_df["TeamNameAlias"].str.contains(
                search_text, case=False, na=False
            )
        ]

    st.dataframe(
        filtered_df[
            [
                "MarketName",
                "TeamName",
                "TeamNameAlias",
                "Founded",
                "Mascot",
                "FightSong",
                "ChampionshipsWon",
                "ConferenceName",
                "Conference_Alias",
                "VenueName",
                "VenueState",
                "VenueCountry",
                "DivisionName",
                "DivisionNameAlias",
            ]
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)
    # Option to view team roster by selecting a team
    team_options = filtered_df[["TeamId", "TeamName"]].drop_duplicates()
    team_display = team_options["TeamName"].tolist()
    selected_team_name = st.selectbox("Select a team to view roster", team_display)

    if selected_team_name:
        # Get the TeamId for the selected team name
        selected_team_id = team_options[team_options["TeamName"] == selected_team_name][
            "TeamId"
        ].values[0]
        # Fetch roster using TeamId
        roster = team_data_model.get_team_roster(selected_team_id)
        st.subheader(f"{selected_team_name} Roster")
        df = pd.DataFrame(roster)
        df.index = df.index + 1
        st.dataframe(df)
