from django.contrib import admin
from .models import Accident, Events, System, Users, Status, Tag, Source

admin.site.register(Accident)
admin.site.register(Events)
admin.site.register(System)
admin.site.register(Users)
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(Source)
