from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    CustomUser,
    MessageBox,
    Transaction,
    Balance,
    MyModel,
    MyTransfer,
    MessageModel
)

# -------------------------------
# Custom User Admin
# -------------------------------
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "username", "password")}),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone_number", "username", "password1", "password2"),
        }),
    )

    list_display = ("phone_number", "username", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("phone_number", "username")
    ordering = ("phone_number",)


# Register CustomUser Admin
admin.site.register(CustomUser, UserAdmin)


# -------------------------------
# MessageBox Admin
# -------------------------------
@admin.register(MessageBox)
class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ("heading", "date", "time")


# -------------------------------
# Transaction Admin
# -------------------------------
class TransactionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # new transaction
            obj.is_new_transaction = True
        super().save_model(request, obj, form, change)

admin.site.register(Transaction, TransactionAdmin)


# -------------------------------
# MyModel Admin
# -------------------------------
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = (
        "name", "amount", "date", "bank_account_number",
        "first_message", "payment_method",
        "confirmation_code", "second_message"
    )


# -------------------------------
# MyTransfer Admin (FIXED NAME ✅)
# -------------------------------
@admin.register(MyTransfer)
class MyTransferAdmin(admin.ModelAdmin):
    list_display = (
        "id", "image", "amount", 
        "message1", "message2", "message3", "message4"
    )


# -------------------------------
# MessageModel Admin
# -------------------------------
@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ("message1", "message2", "message3", "message4")
    list_display_links = ("message1", "message2", "message3", "message4")
    search_fields = ("message1", "message2", "message3", "message4")
    list_per_page = 20


# -------------------------------
# Balance Admin
# -------------------------------
class BalanceAdmin(admin.ModelAdmin):
    list_display = ("available_balance", "ledger_balance")

    @staticmethod
    def available_balance(obj):
        return obj.amount
    available_balance.short_description = "Available Balance"

    @staticmethod
    def ledger_balance(obj):
        return obj.amount1
    ledger_balance.short_description = "Ledger Balance"

admin.site.register(Balance, BalanceAdmin)
