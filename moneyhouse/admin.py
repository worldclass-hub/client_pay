from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, MessageBox, Transaction, Balance
from .models import MyModel, MyTransfer
from .models import MessageModel

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('phone_number', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('phone_number', 'username', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('phone_number', 'username',)
    ordering = ('phone_number',)


@admin.register(MessageBox)
class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ('heading', 'date', 'time')

class TransactionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # Check if it's a new transaction
            obj.is_new_transaction = True
        super().save_model(request, obj, form, change)





@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'bank_account_number', 'first_message', 'payment_method', 'confirmation_code', 'second_message')






@admin.register(MyTransfer)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'amount', 'message1', 'message2', 'message3', 'message4')




@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('message1', 'message2', 'message3', 'message4')
    list_display_links = ('message1', 'message2', 'message3', 'message4')
    search_fields = ('message1', 'message2', 'message3', 'message4')
    list_per_page = 20


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CustomUser, UserAdmin)

admin.site.register(Balance)

