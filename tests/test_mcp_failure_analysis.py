from MCP.failure_analyzer import FailureAnalyzer


def test_mcp_failure_analysis():

    try:

        # simulate Selenium timeout error
        raise Exception(
            "TimeoutException: element not visible"
        )

    except Exception as e:

        analysis = FailureAnalyzer.analyze(e)

        print("\nMCP Analysis Result:")
        print(analysis)

        assert (
            analysis
            ==
            "Page loading slow or locator not visible"
        )