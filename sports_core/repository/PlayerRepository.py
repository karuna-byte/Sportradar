from database.base_repository import BaseRepository


class PlayerRepository(BaseRepository):

    # Insert player method
    def insert_player(self):
        query = """
        INSERT INTO players (player_id, first_name, last_name, abbr_name, birth_place, position, height, weight, status, eligibility, team_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.player_id,
            self.first_name,
            self.last_name,
            self.abbr_name,
            self.birth_place,
            self.position,
            self.height,
            self.weight,
            self.status,
            self.eligibility,
            self.team_id,
        )
        return self.save(query, params)
