import falcon

from src.controllers.images import ImagesController, ItemController
from src.providers.image_store import ImageStore

app = application = falcon.App()

image_store = ImageStore('public/images/')

images_controller = ImagesController(image_store)
item_controller = ItemController(image_store)

app.add_route('/images', images_controller)
app.add_route('/images/{name}', item_controller)
