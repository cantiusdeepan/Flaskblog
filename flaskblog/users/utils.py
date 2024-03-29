import secrets

import os

from PIL import Image
from flask_mail import Message
from flask import url_for,current_app

from flaskblog import mail



def save_picture(form_picture):
    # using random hex to use a random file name for the image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics',
                                picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password reset request!', sender='noreply@polito.it',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_password', token=token, _external=True)}

If you did not make this request, simply ignore this message and nothing 
will be changed!
    '''
    mail.send(msg)


