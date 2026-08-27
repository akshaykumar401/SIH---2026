import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SkillBridge.settings")
django.setup()
from django.conf import settings
settings.ALLOWED_HOSTS = ['*']

from django.test import Client
c = Client(raise_request_exception=True)
c.login(username='testadmin', password='password')

try:
    resp = c.get('/admin/user/user_profile/')
    if resp.status_code == 200:
        print("List view is OK")
    else:
        print(f"List view returned {resp.status_code}")
except Exception as e:
    import traceback
    traceback.print_exc()

