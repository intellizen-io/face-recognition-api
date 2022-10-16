import os


class TestEnv:
    schema = 'http'
    server_ip = 'localhost'
    server_port = '9000'

    @staticmethod
    def get_images_folder():
        return 'api_tests/images' if os.path.isdir('api_tests/images') else os.path.join('.', 'images')
