from django.contrib import admin

from .models import User, workerModel, childModel


#admin.site.register(User)
admin.site.register(workerModel)
admin.site.register(childModel)
