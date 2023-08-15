
def pytest_html_report_title(report):
    from eq.lib.example import __version__ as version
    report.title = f"Test Report for Version {version}"