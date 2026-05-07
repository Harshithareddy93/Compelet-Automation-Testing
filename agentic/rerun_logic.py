def should_rerun(exception):

    retryable_errors = [
        "TimeoutException",
        "StaleElementReferenceException",
        "WebDriverException"
    ]

    return any(error in str(exception) for error in retryable_errors)