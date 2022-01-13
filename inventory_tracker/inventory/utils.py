from flask import current_app
from PIL import Image
import secrets
import os


def save_image(picture_form):
    # Produce a random hex and use that as the image name internally to
    # avoid any possible file name collisions
    random_hex = secrets.token_hex(8)
    _, extension = os.path.splitext(picture_form.filename)
    image_file_name = random_hex + extension
    image_path = os.path.join(current_app.root_path, 'static/item_images', image_file_name)

    # Resize the image to a predefined resolution that will reduce file size
    # and maintain optimal quality
    output_size = (480, 480)
    image_temp = Image.open(picture_form)
    image_temp.thumbnail(output_size)
    image_temp.save(image_path)

    return image_file_name


def delete_image(current):
    if current != 'default.jpg':
        picture_path = os.path.join(current_app.root_path, 'static/item_images', current)
        os.remove(picture_path)
