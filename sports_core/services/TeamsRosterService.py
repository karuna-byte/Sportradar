from sports_core.client import get_api_response


class TeamsRosterService:

    try:

        def fetch_team_roster(team_id):
            endpoint = f"teams/{team_id}/full_roster.json"
            return get_api_response(endpoint)

    except Exception as e:
        print(f"Error fetching team roster: {e}")
