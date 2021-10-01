from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class HomeMenuItem:
    def __init__(self, image_name=None, menu_name=None, url_name=None):
        self.image_name = f"menu_images/{image_name}" if image_name else image_name
        self.menu_name = menu_name
        self.url_name = url_name
