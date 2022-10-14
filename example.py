import json
import base64
import requests

# with open('image_bytes.txt', 'r') as image_b_file:
#     image_data = image_b_file.read()

with open('images/denchik_inst_small.png', 'rb') as image_b_file:
    image_data = base64.b64encode(image_b_file.read())

payload = {
    'image_bytes': image_data
}

response = requests.post(url='http://10.100.102.60:9000/face_exists', json=payload)
print(response.json())
