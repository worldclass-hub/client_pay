from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
   
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import inspect
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
# Your other model definitions...
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from .signals import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType



class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, username=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The phone number must be set')
        user = self.model(phone_number=phone_number, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, username=username, password=password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.username:
            return f"{self.username} ({self.phone_number})"
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser



class MessageBox(models.Model):
    image = models.ImageField(upload_to='messagebox_images/')
    heading = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    paragraph_class = models.CharField(max_length=200, default='default_paragraph_class', blank=True)
    text_Account_name = models.TextField(default='Default Account Name')
    text_Transaction_Type = models.TextField( default='Default Transaction Type')
    text_Transaction_Amount = models.TextField(default='Default Transaction Amount')
    text_Transaction_Currency = models.TextField(default='Default Transaction Currency')
    text_Account_Number = models.TextField(default='Default Account Number')
    text_Transaction_Narration = models.TextField(default='Default Transaction Narration')
    text_Transaction_Remarks = models.TextField(default='Default Transaction Remarks')
    date = models.DateField(null=True)
    time = models.TimeField(default=datetime.now)
    text_Available_Balance = models.TextField(default='Default Available Balance')
    text_Cleared_Balance = models.TextField(default='Default Cleared Balance')
    text_News_Update1 = models.TextField(default='Default News Update1')
    text_News_Update2 = models.TextField(default='Default News Update2')



    def __str__(self):
            return self.heading
    


class Transaction(models.Model):
    image = models.ImageField(upload_to='transaction_images/')
    month = models.DateField()
    amount = models.TextField(default='Default Money Received')
    Recipient_Name = models.TextField(default='Default Recipient Details')
    Sender_Name = models.TextField(default='Default Sender Details')
    Sender_Bank = models.TextField(default='Default Sender Details')
    Sender_Account = models.TextField(default='Default Sender Details')
    Transaction_Type = models.TextField(default='Default Transaction Type')
    Transaction_Number = models.TextField(default='Default Transaction Number')
    Credited_To = models.TextField(default='Default Credited To')
    is_new_transaction = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(auto_now_add=True)
    status_choices = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),  # New status choice
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')

    class Meta:
        ordering = ['-id']

    def is_pending(self):
        return self.status == 'Pending'

    def is_successful(self):
        return self.status == 'Successful'

    def is_failed(self):
        return self.status == 'Failed'

    def get_status_class(self):
        if self.status == 'Pending':
            return 'status-pending'
        elif self.status == 'Successful':
            return 'status-successful'
        elif self.status == 'Failed':
            return 'status-failed'
        else:
            return ''

    def __str__(self):
        return f'Transaction for {self.month}'



    @staticmethod
    def is_transaction_created_from_admin(transaction):
        content_type = ContentType.objects.get_for_model(Transaction)
        log_entries = LogEntry.objects.filter(content_type=content_type, object_id=transaction.id, action_flag=ADDITION)
        return log_entries.exists()

    @staticmethod
    def update_is_new_transaction(sender, instance, created, **kwargs):
        if created and Transaction.is_transaction_created_from_admin(instance):
            instance.is_new_transaction = True
            instance.save(update_fields=['is_new_transaction'])
        elif not created and not hasattr(instance, '_from_admin_panel'):
            if instance.is_new_transaction:
                instance.is_new_transaction = False
                instance.save(update_fields=['is_new_transaction'])




class SentEmail(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    )

    to_email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='sent_emails/images/')
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Email sent to {self.to_email} on {self.sent_at} ({self.status})"





class MyModel(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    date = models.DateField()
    bank_account_number = models.TextField()
    first_message = models.TextField()
    payment_method = models.TextField()
    confirmation_code = models.TextField()
    second_message = models.TextField()

    def __str__(self):
        return self.name




class MyTransfer(models.Model):
    image = models.ImageField(upload_to='images/')
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    message1 = models.TextField()
    message2 = models.TextField()
    message3 = models.TextField()
    message4 = models.TextField()

    def __str__(self):
        return f"Image: {self.image}, Amount: {self.amount}"




class MessageModel(models.Model):
    message1 = models.CharField(max_length=255, default='First Page Instruction')
    message2 = models.CharField(max_length=255, default='Bank number ')
    message3 = models.CharField(max_length=255, default='your Bank Name ')
    message4 = models.CharField(max_length=255, default='Note Instructions')
    message5 = models.CharField(max_length=255, default='Final Note Instructions')


    def __str__(self):
        return f"Message: {self.message1}, {self.message2}, {self.message3}, {self.message4}"
    
    
    
    

class Balance(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    amount1 = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Balance: {self.amount}, Balance1: {self.amount1}"
