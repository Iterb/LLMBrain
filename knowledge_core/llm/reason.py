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
        Given a text and a contextual term, extract all the concise facts related to the contextual term.

        The answer should follow the list format:

        1. Part(s) of input text used : extracted fact
        2. Another part(s) of input text used : another fact

        Always rely on the information given in the text. The number of facts is arbitrary, but do not repeat yourself. 
        If there is nothing in the text about the contextual term just say so. Do not use any of your knowlegde execpt the things you
        find in the text.

        The contextual term is: {keyword}
        """
        prompt_template=f'''[INST] <<SYS>>
        {system_message}
        <</SYS>>

        {prompt} [/INST]'''

        return model(prompt_template)# [0]['generated_text']