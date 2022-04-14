from django.contrib import admin
from atexit import register


from .models import Document, Information

from .models import Information
admin.site.register(Document)
admin.site.register(Information)
