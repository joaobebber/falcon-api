import mimetypes

from falcon import MEDIA_MSGPACK, HTTP_200, HTTP_201
from msgpack import packb

class ImagesController:
  def __init__(self, image_store):
    self._image_store = image_store

  def on_get(self, _req, resp):
    doc = {
      'images': [{ 'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png' }]
    }

    resp.status = HTTP_200
    resp.content_type = MEDIA_MSGPACK
    resp.data = packb(doc, use_bin_type=True)

  def on_post(self, req, resp):
    name = self._image_store.save(req.stream, req.content_type)

    resp.status = HTTP_201
    resp.location = '/images/' + name

class ItemController:
  def __init__(self, image_store):
    self._image_store = image_store

  def on_get(self, _req, resp, name):
    resp.content_type = mimetypes.guess_type(name)[0]
    resp.stream, resp.content_length = self._image_store.open(name)
