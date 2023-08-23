from cortex_system.reasoning.reasoning_tools import PromptTemplate


class ReasonUnit:
    def __init__(self, model, message_bank):
        self.model = model
        self.message_bank = message_bank

    def reason(self, level, prompt, keyword=None):
        system_message = self.message_bank.get_message(level)
        prompt_template = PromptTemplate.generate_prompt(system_message, prompt, keyword)
        return self.model(prompt_template)
