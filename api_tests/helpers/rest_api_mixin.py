import logging
import requests

from api_tests.helpers.test_environment import TestEnv


class RestApiMixin(object):
    @classmethod
    def get_base_url(cls):
        return f"{TestEnv.schema}://{TestEnv.server_ip}{(':' + TestEnv.server_port) if TestEnv.server_port else ''}"

    @classmethod
    def _do_request(cls, request_type: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{cls.get_base_url()}/{endpoint}"

        logging.info(f"Sending {request_type} request to {url}")
        response = requests.request(request_type, url, **kwargs)
        logging.info(f"Got status_code - '{response.status_code}' | content - {response.content}")

        return response

    @classmethod
    def get(cls, endpoint: str):
        """
        :rtype: requests.Response
        :param str endpoint: flask server endpoint
        """
        return cls._do_request("GET", endpoint)

    @classmethod
    def post(cls, endpoint: str, json: dict):
        """
        :param json: payload
        :rtype: requests.Response
        :param str endpoint: flask server endpoint
        """
        return cls._do_request("POST", endpoint, json=json)

    @classmethod
    def delete(cls, endpoint: str, json: dict = None):
        """
        :param json: payload
        :rtype: requests.Response
        :param str endpoint: flask server endpoint
        """
        return cls._do_request("DELETE", endpoint, json=json)
