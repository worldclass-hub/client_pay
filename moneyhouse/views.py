from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MessageBox
from django.http import JsonResponse
from moneyhouse.models import MessageBox
from .models import Transaction
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import MonthYearForm,  PaymentForm
from .models import Transaction, Balance
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponseRedirect

import re
from .models import MessageModel
from datetime import datetime
from .models import Transaction

from django.shortcuts import render, redirect
from .models import MyModel
from django.shortcuts import render, get_object_or_404

from django.db.models import QuerySet
from django.http import HttpResponse


# views.py
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, PaymentForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from django.shortcuts import render
from .forms import EmailForm
from .models import SentEmail
from django.shortcuts import render, redirect
from .models import MyModel

from datetime import datetime
import re
from .models import Transaction
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.conf import settings
from .forms import EmailForm

from django.conf import settings
from django.http import HttpResponseRedirect

# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import EmailForm
# Your view functions here


from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import EmailForm
from django.shortcuts import render, redirect


from .models import MyTransfer
















def index(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey, you are already logged in.")
        return redirect("base")

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        
        # Authenticate user
        user = authenticate(request, username=phone_number, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back, you have been logged in.")
            return redirect("base")
        else:
            messages.warning(request, "User account login does not exist.")
            return redirect("index")  # Redirect back to the login page if user does not exist

    return render(request, 'index.html')

def base(request):
    balance = Balance.objects.first()  # You can retrieve the balance object here

    return render(request, 'base.html', {'balance': balance})

def register_view(request):
    return render(request, "register.html")

def logout_view(request):
    logout(request)
    # Redirect to a success page (change 'success_url_name' to your URL name)
    return redirect('index')




def message_box(request):
    messages = MessageBox.objects.all().order_by('-date', '-time')
    return render(request, 'message_box.html', {'messages': messages})


def message_detail(request, message_id):
    message = MessageBox.objects.get(id=message_id)
    return render(request, 'message_detail.html', {'message': message})


def get_message_count(request):
    count = MessageBox.objects.count()
    return JsonResponse({'count': count})



def all_transactions(request):
    current_year = datetime.now().year
    transactions = Transaction.objects.filter(date__year=current_year).order_by('-date')

    # Get transactions for previous years
    previous_transactions = Transaction.objects.exclude(date__year=current_year).order_by('-date')

    # Combine the transactions
    transactions = list(transactions) + list(previous_transactions)

    total_amount = 0
    for transaction in transactions:
        try:
            amount = float(re.sub(r'[^\d.]', '', transaction.amount))
            total_amount += amount
        except ValueError:
            print(f"Invalid amount for transaction {transaction.id}: {transaction.amount}")

    # Check if there are new transactions
    has_new_transactions = Transaction.objects.filter(is_new_transaction=True).exists()

    # Reset is_new_transaction flag after displaying the bell icon
    for transaction in transactions:
        if transaction.is_new_transaction:
            transaction.is_new_transaction = False
            transaction.save()

    return render(request, 'all_transactions.html', {'transactions': transactions, 'total_amount': total_amount, 'has_new_transactions': has_new_transactions})




def check_new_transactions(request):
    has_new_transactions = Transaction.objects.filter(is_new_transaction=True).exists()
    return JsonResponse({'has_new_transactions': has_new_transactions})





def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})




def get_transactions(request):
    month = request.GET.get('month')
    year = request.GET.get('year')

    # Validate the month and year values
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        return JsonResponse({'error': 'Invalid month or year format'}, status=400)

    if not 1 <= month <= 12:
        return JsonResponse({'error': 'Invalid month value'}, status=400)

    # Assume year is in valid range, e.g., 2000 to 2100
    if not 2000 <= year <= 2100:
        return JsonResponse({'error': 'Invalid year value'}, status=400)

    # Continue with your transaction filtering logic
    transactions = Transaction.objects.filter(date__month=month, date__year=year)

    # Serialize the transactions and return as JSON response
    data = [{'id': transaction.id, 'amount': transaction.amount, 'Sender_Name': transaction.Sender_Name, 'date': transaction.date, 'status': transaction.status, 'time': transaction.time, 'image_url': transaction.image.url} for transaction in transactions]
    return JsonResponse(data, safe=False)





def get_transactions_for_month_year(request):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        transactions = Transaction.objects.filter(month=month, year=year)
        data = [{'id': transaction.id, 'amount': transaction.amount, 'Sender_Name': transaction.Sender_Name, 'date': transaction.date, 'status': transaction.status, 'time': transaction.time, 'image_url': transaction.image.url} for transaction in transactions]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import MyModel
from .forms import EmailForm


def send_email_view(request):
    print("✅ ENTERED send_email_view")     # Debug

    my_model_instance = MyModel.objects.first()

    if not my_model_instance:
        print("❌ No MyModel instance found")
        return HttpResponse("No MyModel instances found.")

    # Extract data
    name = my_model_instance.name
    amount = my_model_instance.amount
    date = my_model_instance.date
    bank_account_number = my_model_instance.bank_account_number
    first_message = my_model_instance.first_message
    payment_method = my_model_instance.payment_method
    Routing_number = my_model_instance.Routing_number
    Bank_Name = my_model_instance.Bank_Name
    Transaction_ID = my_model_instance.Transaction_ID
    second_message = my_model_instance.second_message

    if request.method == 'POST':
        print("✅ POST REQUEST RECEIVED")   # Debug

        form = EmailForm(request.POST)

        if form.is_valid():
            print("✅ FORM IS VALID")        # Debug
            print("✅ ATTEMPTING TO SEND EMAIL...")  # Debug

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = form.cleaned_data['recipients'].split(',')

            html_message = render_to_string('client_template.html', {
                'name': name,
                'amount': amount,
                'date': date,
                'bank_account_number': bank_account_number,
                'first_message': first_message,
                'payment_method': payment_method,
                'Routing_number': Routing_number,
                'Bank_Name': Bank_Name,
                'Transaction_ID': Transaction_ID,
                'second_message': second_message,
                'message': message,
            })

            try:
                send_mail(
                    subject,
                    '',  # Empty text body (HTML only)
                    settings.DEFAULT_FROM_EMAIL,
                    recipients,
                    html_message=html_message,
                    fail_silently=False,
                )
                print("✅ EMAIL SENT SUCCESSFULLY")   # Debug
            except Exception as e:
                print("❌ ERROR SENDING EMAIL:", str(e))  # Debug
                return HttpResponse("Email sending failed: " + str(e))

            return redirect('success')
        else:
            print("❌ FORM INVALID:", form.errors)   # Debug
    else:
        print("✅ GET REQUEST — LOADING FORM")        # Debug
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})


def success(request):
    print("✅ SUCCESS PAGE LOADED")  # Debug
    return render(request, 'success.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name} ({email})',
                message,
                'World Bank <' + settings.EMAIL_HOST_USER + '>',
                ['samuelemenike4321@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def maintainance(request):
    return render(request, 'maintainance.html')



def client_template(request):
    if request.method == 'POST':
        MyModel.objects.create(
            name=request.POST.get('name'),
            amount=request.POST.get('amount'),
            date=request.POST.get('date'),
            bank_account_number=request.POST.get('bank_account_number'),
            first_message=request.POST.get('first_message'),
            payment_method=request.POST.get('payment_method'),
            confirmation_code=request.POST.get('confirmation_code'),
            second_message=request.POST.get('second_message')
        )
        return redirect('success')  # Redirect to a success page or another URL
    
    my_models = MyModel.objects.all()
    return render(request, 'client_template.html', {'my_models': my_models})



def transfer(request):
    my_transfers = MyTransfer.objects.all()
    return render(request, 'transfer.html', {'my_transfers': my_transfers})




def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct the email message
            subject = 'Client Details Submission For Free Money'
            body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

            # Send the email using Django's send_mail function
            send_mail(subject, body, 'World Bank <' + settings.EMAIL_HOST_USER + '>', ['samuelemenike4321@gmail.com'],  fail_silently=False)


            return HttpResponseRedirect('/payment_success/')
    else:
        form = PaymentForm()

    messagings = MessageModel.objects.all()
    return render(request, 'payment.html', {'messagings': messagings})



def payment_success(request):
    return render(request, 'payment_success.html')

def account_statement(request):
    balance = Balance.objects.first()  # You can retrieve the balance object here

    return render(request, 'account_statement.html', {'balance': balance})

    

