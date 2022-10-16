import os
import sys
import requests

from shared_helpers.conversions import image_into_bytes

try:
    SERVER_IP = os.environ["SERVER_IP"]
except KeyError:
    print("Please set the environment variables: SERVER_IP")
    sys.exit(1)


if __name__ == '__main__':
    example_image = 'example_face.jpeg'

    image_bytes = image_into_bytes(image_path=f'example/{example_image}' if not os.path.isfile(example_image) else example_image)

    payload = {
        'image_bytes': str(image_bytes)
    }

    response = requests.post(url=f'http://{SERVER_IP}:9000/face-detection', json=payload)

    if response.ok and response.content:
        print(response.json())
    else:
        print("no data returned from the flask server.")
