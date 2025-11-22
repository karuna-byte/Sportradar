from sports_core.repository.CoachRepository import CoachRepository


class Coach(CoachRepository):
    def __init__(self, coach_id, full_name, position, team_id):
        self.coach_id = coach_id
        self.full_name = full_name
        self.position = position
        self.team_id = team_id

    # Save coach method
    def save_coach(self):
        return self.insert_coach()
