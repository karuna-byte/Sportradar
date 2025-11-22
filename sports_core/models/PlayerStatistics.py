from sports_core.repository.PlayerStatisticsRepository import PlayerStatisticsRepository


class PlayerStatistics(PlayerStatisticsRepository):
    def __init__(
        self,
        player_id,
        team_id,
        season_id,
        games_played,
        games_started,
        rushing_yards,
        rushing_touchdowns,
        receiving_yards,
        receiving_touchdowns,
        kick_return_yards,
        fumbles,
    ):
        self.player_id = player_id
        self.team_id = team_id
        self.season_id = season_id
        self.games_played = games_played
        self.games_started = games_started
        self.rushing_yards = rushing_yards
        self.rushing_touchdowns = rushing_touchdowns
        self.receiving_yards = receiving_yards
        self.receiving_touchdowns = receiving_touchdowns
        self.kick_return_yards = kick_return_yards
        self.fumbles = fumbles

    # Save player statistics method
    def save_player_statistics(self):
        return self.insert_player_statistics()

    # Get all player IDs method
    def fetch_all_player_ids(self):
        return self.get_all_player_ids()
