from database.base_repository import BaseRepository


class PlayerStatisticsRepository(BaseRepository):

    # Insert player statistics method
    def insert_player_statistics(self):
        query = """
        INSERT INTO player_statistics(player_id, team_id, season_id, games_played, games_started, rushing_yards, rushing_touchdowns, receiving_yards, receiving_touchdowns, kick_return_yards, fumbles)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.player_id,
            self.team_id,
            self.season_id,
            self.games_played,
            self.games_started,
            self.rushing_yards,
            self.rushing_touchdowns,
            self.receiving_yards,
            self.receiving_touchdowns,
            self.kick_return_yards,
            self.fumbles,
        )
        return self.save(query, params)

    def get_all_player_ids(self):
        query = "select player_id from players"
        params = ()
        return self.get_all(query, params)
