from database.base_repository import BaseRepository


class TeamRepository(BaseRepository):

    # Insert team method
    def insert_team(self):
        query = """
        INSERT INTO teams (team_id, market, name, alias, founded, mascot, fight_song, championships_won, venue_id, conference_id, division_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.team_id,
            self.market,
            self.name,
            self.alias,
            self.founded,
            self.mascot,
            self.fight_song,
            self.championships_won,
            self.venue_id,
            self.conference_id,
            self.division_id,
        )
        return self.save(query, params)
