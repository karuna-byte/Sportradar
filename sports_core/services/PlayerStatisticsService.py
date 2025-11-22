from sports_core.client import get_api_response
from sports_core.models.PlayerStatistics import PlayerStatistics
import time


class PlayerStatisticsService:

    @staticmethod
    def fetch_player_statistics(player_id):
        endpoint = f"players/{player_id}/profile.json"
        return get_api_response(endpoint)

    @staticmethod
    def get_all_player_ids():
        statistics = PlayerStatistics(
            None, None, None, None, None, None, None, None, None, None, None
        )
        return statistics.fetch_all_player_ids()

    @staticmethod
    def save_player_statistics(player_response, player_id):
        for season in player_response.get("seasons", []):
            try:
                stats = season.get("teams", [{}])[0].get("statistics", {})
                player_stats = PlayerStatistics(
                    player_id=player_id,
                    team_id=season.get("teams", [{}])[0].get("id"),
                    season_id=season.get("id"),
                    games_played=stats.get("games_played", 0),
                    games_started=stats.get("games_started", 0),
                    rushing_yards=stats.get("rushing", {}).get("yards", 0),
                    rushing_touchdowns=stats.get("rushing", {}).get("touchdowns", 0),
                    receiving_yards=stats.get("receiving", {}).get("yards", 0),
                    receiving_touchdowns=stats.get("receiving", {}).get(
                        "touchdowns", 0
                    ),
                    kick_return_yards=stats.get("kick_returns", {}).get("yards", 0),
                    fumbles=stats.get("fumbles", {}).get("fumbles", 0),
                )
                player_stats.save_player_statistics()
            except KeyError as e:
                print(f"Missing key: {e}")
            except Exception as e:
                print(f"Error processing season: {e}")


if __name__ == "__main__":
    try:
        player_dist = PlayerStatisticsService.get_all_player_ids()
        i = 0
        for player in player_dist:
            player_id = player["player_id"]
            player_response = PlayerStatisticsService.fetch_player_statistics(player_id)
            if player_response:
                PlayerStatisticsService.save_player_statistics(
                    player_response, player_id
                )
                time.sleep(2)  # Rate limit
    except Exception as e:
        print(f"Error: {e}")
