import pytest

from api_tests.helpers.test_environment import TestEnv
from api_tests.helpers.rest_api_mixin import RestApiMixin

from shared_helpers.conversions import image_into_bytes


def pytest_addoption(parser):
    parser.addoption("--server-ip", action="store", dest="server_ip", default="localhost")


@pytest.fixture(scope='session', autouse=True)
def server_ip(request):
    TestEnv.storage_ip = request.config.getoption("--server-ip")


def detect_face_by_image(image_file: str):
    image_bytes = image_into_bytes(image_path=f'{TestEnv.get_images_folder()}/{image_file}')
    payload = {'image_bytes': str(image_bytes)}

    return RestApiMixin.post(endpoint='face-detection', json=payload)
