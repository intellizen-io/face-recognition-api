import json
import base64
import requests


with open('images/denchik_inst_small.png', 'rb') as image_b_file:
    image_data = base64.b64encode(image_b_file.read())

payload = {
    'image_bytes': str(image_data)
}

response = requests.post(url='http://10.100.102.60:9000/face-exists', json=payload)
print(response.json())
