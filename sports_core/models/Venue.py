from sports_core.repository.VenueRepository import VenueRepository


class Venue(VenueRepository):
    def __init__(
        self,
        venue_id,
        name,
        city,
        state,
        country,
        zip_code,
        address,
        capacity,
        surface,
        roof_type,
        latitude,
        longitude,
    ):
        self.venue_id = venue_id
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.address = address
        self.capacity = capacity
        self.surface = surface
        self.roof_type = roof_type
        self.latitude = latitude
        self.longitude = longitude

    # Save venue method
    def save_venue(self):
        return self.insert_venue()
