from sports_core.client import get_api_response
from sports_core.services.TeamsRosterService import fetch_team_roster
from sports_core.models.Venue import Venue
from sports_core.models.Conference import Conference
from sports_core.models.Division import Division
from sports_core.models.Team import Team
from sports_core.models.Coach import Coach
from sports_core.models.player import Player
import time


class TeamsService:

    def save_venue(venue_object):
        venue = Venue(
            venue_id=venue_object.get("id"),
            name=venue_object.get("name", None),
            city=venue_object.get("city", None),
            state=venue_object.get("state", None),
            country=venue_object.get("country", None),
            zip_code=venue_object.get("zip", None),
            address=venue_object.get("address", None),
            capacity=venue_object.get("capacity", 0),
            surface=venue_object.get("surface", None),
            roof_type=venue_object.get("roof_type", None),
            latitude=venue_object.get("location", {}).get("lat", 0.0),
            longitude=venue_object.get("location", {}).get("lng", 0.0),
        )

        venue.save_venue()

    def save_conference(conference_object):
        conference = Conference(
            id=conference_object.get("id"),
            name=conference_object.get("name", None),
            alias=conference_object.get("alias", None),
        )
        conference.save_conference()

    def save_division(division_object):
        division = Division(
            id=division_object.get("id"),
            name=division_object.get("name", None),
            alias=division_object.get("alias", None),
        )
        division.save_division()

    def save_team(team_object):
        team = Team(
            team_id=team_object.get("id"),
            market=team_object.get("market", None),
            name=team_object.get("name", None),
            alias=team_object.get("alias", None),
            founded=team_object.get("founded", 0),
            mascot=team_object.get("mascot", None),
            fight_song=team_object.get("fight_song", None),
            championships_won=team_object.get("championships_won", 0),
            venue_id=team_object.get("venue", {}).get("id", None),
            conference_id=team_object.get("conference", {}).get("id", None),
            division_id=team_object.get("division", {}).get("id", None),
        )
        team.save_team()

    def sav_coach(team_roster_response):
        team_id = team_roster_response["id"]
        for team_coach in team_roster_response["coaches"]:
            coach = Coach(
                coach_id=team_coach.get("id"),
                full_name=team_coach.get("full_name", None),
                position=team_coach.get("position", None),
                team_id=team_id,
            )
            coach.save_coach()

    def save_player(team_roster_response):
        team_id = team_roster_response["id"]
        for team_player in team_roster_response["players"]:
            if team_player["status"].upper() == "ACT":
                player = Player(
                    player_id=team_player.get("id"),
                    first_name=team_player.get("first_name", None),
                    last_name=team_player.get("last_name", None),
                    abbr_name=team_player.get("abbr_name", None),
                    birth_place=team_player.get("birth_place", None),
                    position=team_player.get("position", None),
                    height=team_player.get("height", 0),
                    weight=team_player.get("weight", 0),
                    status=team_player.get("status", None),
                    eligibility=team_player.get("eligibility", None),
                    team_id=team_id,
                )
                player.save_player()

    def fetch_teams():
        endpoint = "league/teams.json"
        return get_api_response(endpoint)

    try:
        data = fetch_teams()
        for i in range(len(data["teams"])):  # loop list of teams
            team_id = data["teams"][i]["id"]
            team_roster_response = fetch_team_roster(team_id)
            if team_roster_response is None:
                print(f"Warning: No response for team {team_id}, skipping...")
                time.sleep(3)  # Wait longer if we get an error
                continue
            if (
                team_roster_response.get("venue")
                and team_roster_response.get("conference")
                and team_roster_response.get("division")
                and len(team_roster_response.get("players")) > 0
                and len(team_roster_response.get("coaches")) > 0
            ):
                save_venue(team_roster_response["venue"])
                save_conference(team_roster_response["conference"])
                save_division(team_roster_response["division"])
                save_team(team_roster_response)
                sav_coach(team_roster_response)
                save_player(team_roster_response)
            time.sleep(3)  # To avoid hitting rate limits
    except Exception as e:
        print(f"Error: {e}")
