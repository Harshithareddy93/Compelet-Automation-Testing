class FailureAnalyzer:

    @staticmethod
    def analyze(exception):

        error = str(exception)

        if "TimeoutException" in error:
            return "Page loading slow or locator not visible"

        elif "StaleElementReferenceException" in error:
            return "DOM refreshed before Selenium action"

        elif "NoSuchElementException" in error:
            return "Locator may have changed"

        elif "MaxRetryError" in error:
            return "Selenium Grid connection issue"

        else:
            return "Unknown automation issue"