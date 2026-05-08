import random
import string


class LLMDataGenerator:

    @staticmethod
    def random_email():

        prefix = ''.join(
            random.choices(string.ascii_lowercase, k=6)
        )

        return f"{prefix}@gmail.com"

    @staticmethod
    def random_note_title():

        return "AI Generated Note " + ''.join(
            random.choices(string.ascii_uppercase, k=4)
        )

    @staticmethod
    def random_note_description():

        return "Generated dynamically using MCP framework"