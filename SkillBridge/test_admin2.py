import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SkillBridge.settings")
django.setup()

from django.test import Client
from django.contrib.auth.models import User
c = Client(raise_request_exception=True)
c.login(username='testadmin', password='password')

try:
    c.get('/admin/user/user_profile/')
    print("List OK")
except Exception as e:
    import traceback
    traceback.print_exc()
