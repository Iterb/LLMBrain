from cortex_system.association_cortex.cortical_column import CorticalColumn


class Neocortex:
    def __init__(self):
        self.cortical_columns = []

    def add_cortical_column(self, ku):
        self.cortical_columns.append(ku)

    def display(self):
        for unit in self.cortical_columns:
            print(unit)
