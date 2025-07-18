import os
from django.core.wsgi import get_wsgi_application
# It is Used to Deployment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management.settings')
application = get_wsgi_application()
