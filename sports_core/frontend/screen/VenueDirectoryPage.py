import streamlit as st
import pandas as pd
from sports_core.models.TeamAnalysisViewModel import TeamAnalysisViewModel


def venue_directory_page():
    st.title("🏟️ Venue Directory")

    st.markdown("<br>", unsafe_allow_html=True)

    team_data_model = TeamAnalysisViewModel()
    venue_data = team_data_model.get_venue_info()
    df = pd.DataFrame(venue_data)
    df.index = df.index + 1

    # Sidebar filters
    state = st.sidebar.selectbox(
        "Filter by State", ["All"] + sorted(df["State"].dropna().unique())
    )
    roofType = st.sidebar.selectbox(
        "Filter by RoofType", ["All"] + sorted(df["RoofType"].dropna().unique())
    )

    # Apply filters
    filtered_df = df.copy()
    if state != "All":
        filtered_df = filtered_df[filtered_df["State"] == state]
    if roofType != "All":
        filtered_df = filtered_df[filtered_df["RoofType"] == roofType]

    st.dataframe(
        filtered_df[
            [
                "VenueName",
                "City",
                "State",
                "Country",
                "Zip",
                "Address",
                "Capacity",
                "Surface",
                "RoofType",
                "Latitude",
                "Longitude",
            ]
        ]
    )
