from sports_core.repository.RankingRepository import RankingRepository


class Ranking(RankingRepository):
    def __init__(
        self,
        poll_id,
        poll_name,
        season_id,
        week,
        effective_time,
        team_id,
        ranking,
        prev_rank,
        points,
        fp_votes,
        wins,
        losses,
        ties,
    ):
        self.poll_id = poll_id
        self.poll_name = poll_name
        self.season_id = season_id
        self.week = week
        self.effective_time = effective_time
        self.team_id = team_id
        self.ranking = ranking
        self.prev_rank = prev_rank
        self.points = points
        self.fp_votes = fp_votes
        self.wins = wins
        self.losses = losses
        self.ties = ties

    # Save ranking method
    def save_ranking(self):
        return self.insert_ranking()

    # Fetch all seasons method
    def fetch_all_seasons(self, params=None):
        return self.get_all_season(params)
