from sports_core.repository.DivisionRepository import DivisionRepository


class Division(DivisionRepository):
    def __init__(self, id, name, alias):
        self.id = id
        self.name = name
        self.alias = alias

    # Save division method
    def save_division(self):
        return self.insert_division()
