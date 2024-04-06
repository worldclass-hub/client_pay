from django import forms
from .models import CustomUser
from django import forms

class LoginForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password']




class MonthYearForm(forms.Form):
    month = forms.DateField(widget=forms.SelectDateWidget(empty_label="Choose month"))



class EmailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    recipients = forms.CharField()



class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)


class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

