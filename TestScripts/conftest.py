from SupportLibraries.driver_factory import DriverFactory
import pytest
from appium.webdriver.appium_service import AppiumService
import time
import logging
import FrameworkUtilities.logger_utility as log_utils
from appium.webdriver.appium_service import AppiumService

log = log_utils.custom_logger(logging.INFO)


# @pytest.fixture(scope="session")
# def get_driver(request, platform):
#     print("session_level_setup: Running session level setup.")
#     df = DriverFactory(platform)
#     driver = df.get_driver_instance()
#     driver.reset()
#     session = request.node
#     for item in session.items:
#         cls = item.getparent(pytest.Class)
#         setattr(cls.obj, "driver", driver)
#     yield
#     print("session_level_setup: Running session level teardown.")
#     driver.reset()
#
#
def pytest_addoption(parser):
    parser.addoption("--platform", help="Mobile Platform")
    parser.addoption("--environment", help="Application Environment")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--environment")



DEFAULT_PORT = 4723





def start_server():
    service: AppiumService
    service = AppiumService()
    service.start(args=['--address', '127.0.0.1', '-p', str(DEFAULT_PORT)])
    return service

def stop_server():
    service: AppiumService
    service = AppiumService()
    service.stop()


@pytest.fixture(scope="function")
def oneTimeSetUp(request):
    # start_server()
    log.info("server started")
    time.sleep(15)
    print("Running class setUp")

    wdf = DriverFactory()
    driver = wdf.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print("Running class tearDown")
    #stop_server()
    #log.info("server stoped")

