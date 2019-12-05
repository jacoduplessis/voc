import os

import dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voc.settings')
dotenv.load_dotenv()
application = get_wsgi_application()
