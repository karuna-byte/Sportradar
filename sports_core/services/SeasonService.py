from sports_core.client import get_api_response
from sports_core.models.Season import Season


class SeasonService:
    @staticmethod
    def fetch_season():
        endpoint = f"/league/seasons.json"
        return get_api_response(endpoint)

    def save_season(season_object):
        season = Season(
            season_id=season_object["id"],
            year=season_object["year"],
            start_date=season_object["start_date"],
            end_date=season_object["end_date"],
            status=season_object["status"],
            type_code=season_object["type"]["code"],
        )
        season.save_season()

    try:
        season_data = fetch_season()
        if season_data["seasons"] is not None:
            for season in season_data["seasons"]:
                save_season(season)

    except Exception as e:
        print(f"Error fetching season data: {e}")
