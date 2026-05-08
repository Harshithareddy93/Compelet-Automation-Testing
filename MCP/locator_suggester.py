class LocatorSuggester:

    @staticmethod
    def suggest(locator):

        if "xpath" in locator.lower():

            return "Try CSS_SELECTOR for better stability"

        elif "id" in locator.lower():

            return "ID locator is stable"

        else:

            return "Consider relative XPath"