# different level of data representatation

import re


class SynapticLearner:
    def __init__(self, reason):
        self.reason = reason

    def process_input(self, text):
        # Extract the facts using regular expression
        facts = re.findall(r"\d+\.\s(.*?)(?=\n|$)", text)
        return [fact for fact in facts]

    def create_input_representation(self, level, prompt, keyword=None):
        return self.reason.reason(level, prompt, keyword)

    def consolidate(self):
        # This is where repeated information would be strengthened.
        # Placeholder for now.
        pass

    # def retrieve(self, keyword):
    #     # Search the KB for a specific keyword and return it if found.
    #     # Simultaneously, reinforce its weight/significance.
    #     for unit in self.kb.top_level_units:
    #         if unit.title == keyword:
    #             # Reinforce (increase weight or adjust position).
    #             # Placeholder for now.
    #             return unit.content
    #     return None

    def prune(self):
        # Analyze the KB and prune out "forgotten" or less significant data.
        # Placeholder for now.
        pass

    # get a chunk of text
    # tell llm to describe its contents in a few words
    # get the embedding of the result
    # check all the top level embedding and find whether the is a similar embedding if not create one
    # then tell llm to describe its contents in a mid level connect knowing that its main embedding
    # get the embedding of the result
    # check all the mid level embedding and find whether the is a similar embedding if not create one

    # on the lowest level we might put entire summarization with the most important facts

    # there may be more then one top level ideas

    # Give me most abstract words that describe below text
    # Science, History, Scientists
    # Tell me about the ideas of this text considering the Science/...//../
    # 1.Einstein theory of relativity
    # Give me as much details as possible on Einstein theory of relativity given this text
