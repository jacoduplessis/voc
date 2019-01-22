import os
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voc.settings')
dotenv.read_dotenv(Path(__file__).parent.parent / '.env')
application = get_wsgi_application()
