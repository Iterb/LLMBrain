# different level of data representatation

class Learner:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def process_input(self, text):
        # Here, we'd typically employ an LLM to parse the text and extract keywords/entities.
        # For now, let's just split the text into words (simplistic approach).
        return text.split()

    def store(self, processed_data):
        for word in processed_data:
            # For now, let's just create a new KU for each word and add to KB.
            # In a real-world scenario, this would be far more nuanced.
            self.kb.add_ku(KnowledgeUnit(word, word))

    def consolidate(self):
        # This is where repeated information would be strengthened.
        # Placeholder for now.
        pass

    def retrieve(self, keyword):
        # Search the KB for a specific keyword and return it if found.
        # Simultaneously, reinforce its weight/significance.
        for unit in self.kb.top_level_units:
            if unit.title == keyword:
                # Reinforce (increase weight or adjust position).
                # Placeholder for now.
                return unit.content
        return None

    def prune(self):
        # Analyze the KB and prune out "forgotten" or less significant data.
        # Placeholder for now.
        pass


    # get a chunk of text 
    # tell llm to describe its contents in a few words 
    # get the embedding of the result
    # check all the top level embbeding and find wheter the is a similar embeding if not create one
    # then tell llm to describe its contents in a mid level conect knowing that its main embeding
    # get the embedding of the result
    # check all the mid level embbeding and find wheter the is a similar embeding if not create one
    
    # on the lowest level we might put entire summarization with the most important facts
    
    # there may be more then one top level ideas
    
    # Give me most abstract words that describe below text
    # Science, History, Scientists
    # Tell me about the ideas of this text considering the Science/...//../
    # 1.Einstein theory of relativity
    # Give me as much details as possible on Einstein theory of relativity given this text