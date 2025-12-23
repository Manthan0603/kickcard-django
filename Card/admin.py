from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username']

class listview(admin.ModelAdmin):
    list_display = ['id', 'KickCardNumber','CustomerFullName']

# class CancelView(admin.ModelAdmin):
#     list_display = ['user']

admin.site.register(User, UserAdmin)
# admin.site.register(KickCard)
admin.site.register(KickCard,listview)
admin.site.register(CancelKickCard)
admin.site.register(BookedRation)
admin.site.register(ContectUs)
