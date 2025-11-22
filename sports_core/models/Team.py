from sports_core.repository.TeamRepository import TeamRepository


class Team(TeamRepository):
    def __init__(
        self,
        team_id,
        market,
        name,
        alias,
        founded,
        mascot,
        fight_song,
        championships_won,
        venue_id,
        conference_id,
        division_id,
    ):
        self.team_id = team_id
        self.market = market
        self.name = name
        self.alias = alias
        self.founded = founded
        self.mascot = mascot
        self.fight_song = fight_song
        self.championships_won = championships_won
        self.venue_id = venue_id
        self.conference_id = conference_id
        self.division_id = division_id

    # Save team method
    def save_team(self):
        return self.insert_team()
