class ReasonUnit:
    # def __init__(self):
    #     pass

    def top_level_reason(self, prompt, model):
        system_message = """
        Your task is to analyze the provided text and identify up to four general concepts or keywords. This process should exclude specific details, names, and granular information. For example, if you receive a text about Einstein, you might return:

            1. Scientist
            2. Physics
            3. Science
            4. History.
            Provide ONLY the keywords, enumerated, without any additional details or explanations.
        """
        prompt_template=f'''[INST] <<SYS>>
        {system_message}
        <</SYS>>

        {prompt} [/INST]'''

        return model(prompt_template)# [0]['generated_text']
    
    def middle_level_reason(self, prompt, model, keyword):
        system_message = f"""
        Given the keyword provided, delve into the text and extract 
        middle-level ideas or terms directly related to that keyword. For instance, if the source text is about Einstein 
        and the keyword is "Scientist," you might return "1. Albert Einstein". If the
        keyword is "Physics", appropriate responses might include "1. Special Relativity 2. General Relativity 3. Theory of Mechanics", etc.
        
        The list can be short (even 1 element but up to 4), but it is crucial that you provide only the terms that are directly in the text.
        Do not provide any information that is not in the text. Also place the most accurate elements on the top.
        
        List these terms in an enumerated format without any further explanations or details.
        
        The keyword is: {keyword}
        """
        prompt_template=f'''[INST] <<SYS>>
        {system_message}
        <</SYS>>

        {prompt} [/INST]'''

        return model(prompt_template)# [0]['generated_text']
    
    def bottom_level_reason(self, prompt, model, keyword):
        system_message = f"""
        Given a text and a contextual term {keyword}, extract the list of facts from text that DIRECTLY and STRICTLY describe to the term {keyword}. If a fact does not mention or inherently imply the {keyword}, DO NOT include it. 

        If there is nothing in the text that mentions or inherently implies {keyword}, simply respond with "NOTHING FOUND". 
        
        Otherwise, the answer should follow the list format, where the each entry is one fact (extracted from text) about {keyword}.
        
        The number of facts is arbitrary, but do not repeat yourself. 
        Use only the provided text to make your decision, do not rely on any of your external knowledge.
        """
        prompt_template=f'''[INST] <<SYS>>
        {system_message}
        <</SYS>>

        {prompt} [/INST]'''

        return model(prompt_template)# [0]['generated_text']