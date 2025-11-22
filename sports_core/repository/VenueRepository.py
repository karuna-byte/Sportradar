from database.base_repository import BaseRepository


class VenueRepository(BaseRepository):

    # Insert venue method
    def insert_venue(self):
        query = """
        INSERT INTO venues (venue_id, name, city, state, country, zip, address, capacity, surface, roof_type, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.venue_id,
            self.name,
            self.city,
            self.state,
            self.country,
            self.zip_code,
            self.address,
            self.capacity,
            self.surface,
            self.roof_type,
            self.latitude,
            self.longitude,
        )
        return self.save(query, params)
