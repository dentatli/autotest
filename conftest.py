import allure
import pytest

from utils.driver_factory import build_driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def driver(request):
    driver = build_driver()
    yield driver

    try:
        failed = request.node.rep_call.failed
    except Exception:
        failed = False

    if failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

        try:
            allure.attach(
                driver.page_source,
                name="page_source",
                attachment_type=allure.attachment_type.HTML,
            )
        except Exception:
            pass

        try:
            allure.attach(
                driver.current_url,
                name="current_url",
                attachment_type=allure.attachment_type.TEXT,
            )
        except Exception:
            pass

    driver.quit()