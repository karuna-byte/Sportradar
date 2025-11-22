from database.base_repository import BaseRepository


class RankingRepository(BaseRepository):

    # Insert ranking method
    def insert_ranking(self):
        query = """
        INSERT INTO rankings(poll_id, poll_name, season_id, week, effective_time, team_id, ranking, prev_rank, points, fp_votes, wins, losses, ties)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.poll_id,
            self.poll_name,
            self.season_id,
            self.week,
            self.effective_time,
            self.team_id,
            self.ranking,
            self.prev_rank,
            self.points,
            self.fp_votes,
            self.wins,
            self.losses,
            self.ties,
        )
        return self.save(query, params)

    # Get all seasons method
    def get_all_season(self, params=None):
        query = "select season_id, year, start_date, end_date from seasons"
        return self.get_all(query, params)
