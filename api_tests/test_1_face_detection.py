import pytest
import multiprocessing

from api_tests.conftest import detect_face_by_image
from api_tests.helpers.base_test_classes import BaseTestClass


@pytest.mark.sanity
class TestFaceDetection(BaseTestClass):

    def test_face_detection_one_request(self):
        response = detect_face_by_image('face_1.jpg')
        assert response.ok
        assert response.json()

        parsed_content = response.json()

        assert parsed_content['face_detection']
        assert len(parsed_content['locations']) > 0
        assert parsed_content['request_came_from']

    def test_face_detection_two_requests_simultaneously(self):
        pool = multiprocessing.Pool(processes=2)
        responses = pool.map(detect_face_by_image, ['face_1.jpg', 'face_2.jpg'])

        for response in responses:
            assert response.ok
            assert response.json()

            parsed_content = response.json()

            assert parsed_content['face_detection']
            assert len(parsed_content['locations']) > 0
            assert parsed_content['request_came_from']

    def test_face_detection_small_image(self):
        response = detect_face_by_image('small_image.jpg')
        assert response.ok
        assert response.json()

        parsed_content = response.json()

        assert parsed_content['face_detection']
        assert len(parsed_content['locations']) > 0
        assert parsed_content['request_came_from']

    def test_face_detection_big_image(self):
        response = detect_face_by_image('big_image.jpg')
        assert response.ok
        assert response.json()

        parsed_content = response.json()

        assert parsed_content['face_detection']
        assert len(parsed_content['locations']) > 0
        assert parsed_content['request_came_from']

    def test_face_detection_no_face(self):
        response = detect_face_by_image('no_face.jpg')
        assert response.ok
        assert response.json()

        parsed_content = response.json()

        assert not parsed_content['face_detection']
        assert len(parsed_content['locations']) == 0
        assert parsed_content['request_came_from']
