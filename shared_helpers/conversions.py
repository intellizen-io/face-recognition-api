import base64
import json
import struct
import logging
from typing import Union
from flask import request


def convert_string_to_bytes(string: str) -> bytes:
    """
    convert string to bytes
    """
    ret_bytes = b''
    for i in string:
        ret_bytes += struct.pack("B", ord(i))
    return ret_bytes


def image_into_bytes(image_path: str) -> bytes:
    """
    open an image and return bytes object
    """
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    encoded = base64.b64encode(image_bytes)
    return encoded


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
