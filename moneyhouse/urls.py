from django.urls import path
from .import views 
from django.contrib.auth import views as auth_views
from .views import message_box, message_detail


urlpatterns = [
    path('', views.index, name = 'index'),
    path('base/', views.base, name = 'base'),
    path('logout/', views.logout_view, name='logout'),
    path('message/', message_box, name='message_box'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('get_message_count/', views.get_message_count, name='get_message_count'),
    path('transactions/', views.all_transactions, name='all_transactions'),
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('api/transactions/', views.get_transactions, name='get_transactions'),
    path('api/transactions/', views.get_transactions_for_month_year, name='get_transactions_for_month_year'),
    path('check_new_transactions/', views.check_new_transactions, name='check_new_transactions'),
    path('send_email/', views.send_email_view, name='send_email'),
    path('success/', views.success, name='success'),  # Add this line
    path('maintainance/', views.maintainance, name='maintainance'),  # Add this line
    path('contact/', views.contact_view, name='contact'),
    path('client_template/', views.client_template, name='client_template'),
    path('transfer/', views.transfer, name='transfer'),
    path('payment/', views.payment_view, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),  # Add this line
    path('account_statement/', views.account_statement, name='account_statement'),  # Add this line

    # path('payment/', views.payment_view_transfer, name='payment'),



]
