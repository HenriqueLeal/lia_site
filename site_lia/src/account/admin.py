from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

#admin.site.register(Account)

class AccountAdmin(UserAdmin): #tambem sobreescrevendo o metodo padrao do django
    list_display = ('email', 'username', 'date_joined', 'last_login',
                    'is_admin', 'is_staff') #campos que serão visiveis
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () #tem que estar aqui pois é required

admin.site.register(Account, AccountAdmin)