from database.base_repository import BaseRepository


class ConferenceRepository(BaseRepository):

    # Insert conference method
    def insert_conference(self):
        query = """
        INSERT INTO conferences (conference_id, name, alias)
        VALUES (%s, %s, %s)
        """
        params = (self.id, self.name, self.alias)
        return self.save(query, params)
