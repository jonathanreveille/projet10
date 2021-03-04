from settings.base import *

load_dotenv()
SECRET_KEY_TRAVIS = os.getenv("SECRET_KEY_TRAVIS")


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
