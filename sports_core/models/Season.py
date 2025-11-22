from sports_core.repository.SeasonRepository import SeasonRepository


class Season(SeasonRepository):
    def __init__(self, season_id, year, start_date, end_date, status, type_code):
        self.season_id = season_id
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.type_code = type_code

    # Save season method
    def save_season(self):
        return self.insert_season()
