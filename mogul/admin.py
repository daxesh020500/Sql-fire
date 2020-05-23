from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Train)
admin.site.register(Train_Status)
admin.site.register(Reservation)
admin.site.register(Route)
admin.site.register(Station)
admin.site.register(consist_of)
admin.site.register(Passenger)
