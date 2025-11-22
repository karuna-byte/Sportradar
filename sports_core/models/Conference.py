from sports_core.repository.ConferenceRepository import ConferenceRepository


class Conference(ConferenceRepository):
    def __init__(self, id, name, alias):
        self.id = id
        self.name = name
        self.alias = alias

    # Save conference method
    def save_conference(self):
        return self.insert_conference()
