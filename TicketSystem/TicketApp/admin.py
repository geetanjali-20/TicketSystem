from django.contrib import admin
from .models import Ticket
from .models import registers
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import newuser

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class NewuserInline(admin.StackedInline):
    model = newuser
    can_delete = False
    verbose_name_plural = 'newusers'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [NewuserInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(newuser)

# Register your models here.
admin.site.register(registers)
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('status', 'assignee')
	list_display = ('id', 'title', 'status', 'assignee', 'description', 'updated_at')
	search_fields = ['title','status']

admin.site.register(Ticket, TicketAdmin)
