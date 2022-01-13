from flask import current_app
import secrets
import os
from PIL import Image


def save_image(picture_form):  # we make a random hex study this method
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(picture_form.filename)
    image_fn = random_hex + ext
    picture_path = os.path.join(current_app.root_path, 'static/item_images', image_fn)
    # resize
    output_size = (480, 480)
    i = Image.open(picture_form)
    i.thumbnail(output_size)
    i.save(picture_path)
    return image_fn


def delete_image(current):
    if current != 'default.jpg':
        picture_path = os.path.join(current_app.root_path, 'static/item_images', current)
        os.remove(picture_path)
