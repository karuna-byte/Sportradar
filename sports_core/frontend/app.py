import streamlit as st
from sports_core.frontend.screen.HomePage import home_page
from sports_core.frontend.screen.TeamsExplorer import teams_explorer_page
from sports_core.frontend.screen.PlayersExplorer import players_explorer_page
from sports_core.frontend.screen.VenueDirectoryPage import venue_directory_page
from sports_core.frontend.screen.SeasonAndScheduleViewerPage import (
    season_and_schedule_viewer_page,
)
from sports_core.frontend.screen.CoachesExplorerPage import coaches_explorer_page
from sports_core.frontend.screen.RankingExplorerPage import ranking_explorer_page
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


st.set_page_config(page_title="Simple Menu App", layout="wide")

st.sidebar.title("Sportradar App")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Teams Explorer",
        "Players Explorer",
        "Season & Schedule Viewer",
        "Ranking Explorer",
        "Venue Directory",
        "Coaches Explorer",
    ],
)

if menu == "Home":
    home_page()
elif menu == "Teams Explorer":
    teams_explorer_page()
elif menu == "Players Explorer":
    players_explorer_page()
elif menu == "Season & Schedule Viewer":
    season_and_schedule_viewer_page()
elif menu == "Venue Directory":
    venue_directory_page()
elif menu == "Coaches Explorer":
    coaches_explorer_page()
elif menu == "Ranking Explorer":
    ranking_explorer_page()
