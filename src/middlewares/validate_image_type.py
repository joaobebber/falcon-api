from falcon import HTTPBadRequest

from src.config.allowed_image_types import ALLOWED_IMAGE_TYPES

def validate_image_type(req, _resp, _resource, _params):
  if req.content_type not in ALLOWED_IMAGE_TYPES:
    msg = 'Image type not allowed. Must be PNG, JPEG, or GIF'

    raise HTTPBadRequest(title='Bad request', description=msg)
