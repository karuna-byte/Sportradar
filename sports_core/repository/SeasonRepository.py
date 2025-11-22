from database.base_repository import BaseRepository


class SeasonRepository(BaseRepository):

    # Insert season method
    def insert_season(self):
        query = """
        INSERT INTO seasons(season_id, year, start_date, end_date, status, type_code)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (
            self.season_id,
            self.year,
            self.start_date,
            self.end_date,
            self.status,
            self.type_code,
        )
        return self.save(query, params)
