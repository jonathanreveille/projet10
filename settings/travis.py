from settings.base import *
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = 'qlksndkljqnsdkjqnsdqnjsd203921Kqlskdnqsdqsd'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
