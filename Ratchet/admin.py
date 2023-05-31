from django.contrib import admin
from .models import Feedback, Employees, Review, Service, Client


admin.site.register(Feedback)
admin.site.register(Employees)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Client)

