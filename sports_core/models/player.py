from sports_core.repository.PlayerRepository import PlayerRepository


class Player(PlayerRepository):
    def __init__(
        self,
        player_id,
        first_name,
        last_name,
        abbr_name,
        birth_place,
        position,
        height,
        weight,
        status,
        eligibility,
        team_id,
    ):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.abbr_name = abbr_name
        self.birth_place = birth_place
        self.position = position
        self.height = height
        self.weight = weight
        self.status = status
        self.eligibility = eligibility
        self.team_id = team_id

    # Save player method
    def save_player(self):
        return self.insert_player()
