from django.contrib import admin

from .models import User, RefCode, VerificationCode

admin.site.register(User)
admin.site.register(RefCode)
admin.site.register(VerificationCode)
