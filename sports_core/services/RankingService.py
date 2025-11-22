from sports_core.models.Ranking import Ranking
from sports_core.client import get_api_response
import time


class RankingService:

    def fetch_rankings_by_weekly(season_year, week_number):
        endpoint = f"polls/AP25/{season_year}/{week_number}/rankings.json"
        return get_api_response(endpoint)

    def save_rankings(ranking_response, season_id):
        if ranking_response.get("rankings") is None:
            return
        if season_id == "17d91be7-4bd3-4407-80e2-eca205c9284a":
            return
        for ranking_entry in ranking_response["rankings"]:
            try:
                ranking_obj = Ranking(
                    poll_id=ranking_response.get("poll", {}).get("id", None),
                    poll_name=ranking_response.get("poll", {}).get("name", None),
                    season_id=season_id,
                    week=ranking_response.get("week", None),
                    effective_time=ranking_response.get("effective_time", None),
                    team_id=ranking_entry.get("id", None),
                    ranking=ranking_entry.get("rank", 0),
                    prev_rank=ranking_entry.get("prev_rank", 0),
                    points=ranking_entry.get("points", 0),
                    fp_votes=ranking_entry.get("fp_votes", 0),
                    wins=ranking_entry.get("wins", 0),
                    losses=ranking_entry.get("losses", 0),
                    ties=ranking_entry.get("ties", 0),
                )
                ranking_obj.save_ranking()
            except KeyError as e:
                print(f"Missing key: {e}")
            except Exception as e:
                print(f"Error processing ranking entry: {e}")

    @staticmethod
    def get_all_seasons():
        ranking = Ranking(
            None, None, None, None, None, None, None, None, None, None, None, None, None
        )
        return ranking.fetch_all_seasons()

    try:
        season_dist = get_all_seasons()
        for season in season_dist:
            if season["season_id"] == "17d91be7-4bd3-4407-80e2-eca205c9284a":
                continue
            weeks = (season["end_date"] - season["start_date"]).days // 7
            for week in range(1, weeks + 1):
                ranking_data = fetch_rankings_by_weekly(season["year"], week)
                if ranking_data:
                    save_rankings(ranking_data, season["season_id"])
                time.sleep(2)  # To avoid hitting API rate limits
    except Exception as e:
        print(f"Error:{e}")
