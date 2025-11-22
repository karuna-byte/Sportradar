from database.base_repository import BaseRepository


class DivisionRepository(BaseRepository):

    # Insert division method
    def insert_division(self):
        query = """
        INSERT INTO divisions (division_id, name, alias)
        VALUES (%s, %s, %s)
        """
        params = (self.id, self.name, self.alias)
        return self.save(query, params)
