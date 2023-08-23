import numpy as np


class CorticalColumn:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.embedding = self.compute_embedding(state)

    def __repr__(self):
        if self.parent:
            return f"CC's memory: {self.state}, CC's parent memory: {self.parent.state}"
        else:
            return f"CC's memory: {self.state}"

    def compute_embedding(self, text):
        #    Placeholder: Integrate with an embedding model.
        return np.random.randn(300)


# make links to similar nodes
#
