import io
import base64
import face_recognition
from flask import request, jsonify, Blueprint

from shared_helpers.loggers import get_logger
from shared_helpers.conversions import verify_json_structure

logger = get_logger(__file__)
blueprint = Blueprint("face_recognition_blueprint", __name__)
backends = [
    'opencv',
    'ssd',
    'dlib',
    'mtcnn',
    'retinaface',
    'mediapipe'
]


@blueprint.route('/face-detection', methods=['POST'])
def face_detection():
    logger.debug("Got new request to face-detection endpoint")
    payload = verify_json_structure(['image_bytes'])
    image_data = base64.b64decode(eval(payload['image_bytes']))

    images_np_data = face_recognition.load_image_file(io.BytesIO(image_data))
    locations = face_recognition.face_locations(images_np_data)

    logger.debug(f"Found {len(locations)} faces")
    return jsonify(
        face_detection=len(locations) > 0,
        locations=locations,
        request_came_from=request.remote_addr
    ), 200
