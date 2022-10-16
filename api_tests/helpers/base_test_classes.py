import pytest

from api_tests.helpers.rest_api_mixin import RestApiMixin


@pytest.mark.sanity
class BaseTestClass:

    @pytest.fixture(scope="session", autouse=True)
    def test_healthcheck(self):
        response = RestApiMixin.get(endpoint='healthcheck')
        assert response.ok
        assert response.json()
        parsed_content = response.json()
        assert parsed_content['status'] == 'success'
