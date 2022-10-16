import os
import sys
import base64
import requests

from helpers.conversions import image_into_bytes

try:
    SERVER_IP = os.environ["SERVER_IP"]
except KeyError:
    print("Please set the environment variables: SERVER_IP")
    sys.exit(1)


if __name__ == '__main__':
    image_bytes = image_into_bytes(image_path='images/example_face.jpeg')
    encoded_image_bytes = base64.b64encode(image_bytes)

    payload = {
        'image_bytes': str(encoded_image_bytes)
    }

    response = requests.post(url=f'http://{SERVER_IP}:9000/face-exists', json=payload)

    if response.ok and response.content:
        print(response.json())
    else:
        print("no data returned from the flask server.")
