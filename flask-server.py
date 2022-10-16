#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys
import json
import base64
import struct
import logging
import face_recognition
from typing import Union
from flask import Flask, request, jsonify

app = Flask(__name__)
backends = [
    'opencv',
    'ssd',
    'dlib',
    'mtcnn',
    'retinaface',
    'mediapipe'
]


def verify_json_structure(keys: list = None) -> Union[dict, tuple]:
    try:
        data = request.get_data().decode('utf8')
        payload = json.loads(data)
    except Exception as e:
        logging.error(f"There was an issue with the provided data. Reason - '{e}'")
        return "Bad request (syntax). please check the sent data.", 400

    try:
        assert isinstance(payload, dict)
        assert all(key in payload.keys() for key in keys)
    except AssertionError:
        return "Bad request. please check the sent data.", 400

    return payload


@app.route('/face-exists', methods=['POST'])
def face_exists():
    payload = verify_json_structure(['image_bytes'])
    image_data = base64.b64decode(eval(payload['image_bytes']))

    images_np_data = face_recognition.load_image_file(io.BytesIO(image_data))
    locations = face_recognition.face_locations(images_np_data)
    return jsonify(
        face_exists=len(locations) > 0,
        locations=locations,
        request_came_from=request.remote_addr
    ), 200


def convert_string_to_bytes(string):
    ret_bytes = b''
    for i in string:
        ret_bytes += struct.pack("B", ord(i))
    return ret_bytes


def image_into_bytes(image_path: str) -> bytes:
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    return image_bytes


if __name__ == '__main__':
    try:
        logging.info('Starting app... Press CTRL+C to quit.')
        app.run(host="0.0.0.0", port=9000)
    except KeyboardInterrupt:
        logging.info('Quitting... (CTRL+C pressed)')
        sys.exit(0)
    except Exception:  # Catch-all for unexpected exceptions, with stack trace
        logging.exception(f'Unhandled exception occurred!')
        sys.exit(1)
