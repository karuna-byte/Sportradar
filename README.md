# Sportradar NCAA Football Analytics Platform

## Overview

This project is a full-stack analytics platform for NCAA Football, built to aggregate, analyze, and visualize data about teams, players, venues, rankings, and schedules. It uses Python for backend data processing and Streamlit for interactive dashboards.

## Features

- **Teams Explorer:** Filter and search NCAA football teams by conference, division, state, or name/alias. View team rosters.
- **Players Explorer:** Browse player details and statistics.
- **Venue Directory:** Explore venue information and locations.
- **Season & Schedule Viewer:** View season details and game schedules.
- **Rankings Explorer:** Analyze team rankings with filters for season, week, and rank range.
- **Data Models:** Relational models for teams, players, venues, rankings, and more.
- **Repository Pattern:** Clean separation of data access logic.
- **Streamlit Frontend:** Interactive dashboards and data tables.

## Project Structure

```
Sportradar/
├── sports_core/
│   ├── models/
│   │   ├── TeamAnalysisViewModel.py
│   │   ├── Venue.py
│   │   └── ...
│   ├── repository/
│   │   ├── VenueRepository.py
│   │   └── ...
│   └── frontend/
│       ├── app.py
│       └── screen/
│           ├── HomePage.py
│           ├── TeamsExplorer.py
│           ├── PlayersExplorer.py
│           ├── VenueDirectoryPage.py
│           ├── SeasonAndScheduleViewerPage.py
│           └── RankingExplorerPage.py
├── database/
│   ├── base_repository.py
│   └── connection.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Streamlit](https://streamlit.io/)
- MySQL or compatible database

### Installation

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd Sportradar
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your database:**
    - Configure connection details in `database/connection.py`.
    - Run migrations or create tables as needed.

4. **Run the Streamlit app:**
    ```bash
    cd sports_core/frontend
    streamlit run app.py
    ```

## Usage

- Use the sidebar to navigate between dashboards.
- Filter, search, and explore NCAA football data interactively.
- View team rosters, player stats, venue info, rankings, and schedules.

## Acknowledgments

- [Sportradar](https://sportradar.com/) for API/data inspiration
- [Streamlit](https://streamlit.io/) for rapid dashboard development
