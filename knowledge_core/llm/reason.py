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
    
    def bottom_level_reason(self, prompt, model, keyword1, keyword2):
        system_message = f"""
        Upon receiving a specific term paired with a more general keyword, your task is to extract detailed, 
        yet concise information related to that specific keywords. 
        For instance, if the text is about Albert Einstein and the terms provided are "Scientist" and "Albert Einstein," 
        potential responses could be:

        1. 14 March 1879 - 18 April 1955: German-born theoretical physicist.
        2. Developed the theory of relativity; contributed to quantum mechanics.
        3. Received the 1921 Nobel Prize in Physics.
        
        Your responses should be brief but rich in detail. List these items in an 
        enumerated format without extraneous explanations or details. If connecting t
        he two terms does not make sense or isn't possible with the text, please indicate this clearly. 
        Always rely solely on the information present in the text.
        The keywords are: {keyword1}, {keyword2}
        """
        prompt_template=f'''[INST] <<SYS>>
        {system_message}
        <</SYS>>

        {prompt} [/INST]'''

        return model(prompt_template)# [0]['generated_text']