import numpy as np


class KnowledgeUnit:
    def __init__(self, title, level, text):
        self.text = text
        self.level = level  # 'Top-Level', 'Mid-Level', 'Fine-Grained'
        self.embedding = self.compute_embedding(text)
        self.related_chunks = []  # This will hold references to related KnowledgeChunks
        
    def add_subunit(self, ku):
        self.subunits.append(ku)
        
    def compute_embedding(self, text):
    #    Placeholder: Integrate with an embedding model like Word2Vec, FastText, etc.
        return np.random.randn(300)
        
        
# make links to similar nodes
# 