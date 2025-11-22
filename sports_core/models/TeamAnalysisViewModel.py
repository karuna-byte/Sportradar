from sports_core.repository.TeamAnalysisViewModelRepository import (
    TeamAnalysisViewModelRepository,
)


class TeamAnalysisViewModel(TeamAnalysisViewModelRepository):

    # Get all team info method
    def get_all_team_info(self, params=None):
        return self.fetch_all_team_info(params)

    # Get all players info method
    def get_all_players_info(self, params=None):
        return self.fetch_all_players_info(params)

    # Get season info method
    def get_season_info(self, params=None):
        return self.fetch_seasons_info(params)

    # Get team roster method
    def get_team_roster(self, team_id):
        return self.fetch_team_roster(team_id)

    # Get venue info method
    def get_venue_info(self):
        return self.fetch_venue_info()

    # Get coach info method
    def get_coach_info(self):
        return self.fetch_coach_info()

    # Get ranking info method
    def get_ranking_info(self):
        return self.fetch_ranking_info()
