class KnowledgeBase:
    def __init__(self):
        self.top_level_units = []

    def add_ku(self, ku, parent_title=None):
        if parent_title:
            for unit in self.top_level_units:
                if unit.title == parent_title:
                    unit.add_subunit(ku)
                    return
                # This can be enhanced to search recursively in subunits too.
        else:
            self.top_level_units.append(ku)

    def display(self, unit=None, indent=0):
        if not unit:
            for u in self.top_level_units:
                self.display(u)
        else:
            print(' ' * indent + unit.title)
            for sub in unit.subunits:
                self.display(sub, indent + 4)