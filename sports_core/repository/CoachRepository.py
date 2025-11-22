from database.base_repository import BaseRepository


class CoachRepository(BaseRepository):

    # Insert coach method
    def insert_coach(self):
        query = """
        INSERT INTO coaches(coach_id, full_name, position, team_id)
        VALUES (%s, %s, %s, %s)
        """
        params = (self.coach_id, self.full_name, self.position, self.team_id)
        return self.save(query, params)
