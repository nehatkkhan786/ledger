from django.urls import path
from .views import *


urlpatterns = [

path('', HomepageView.as_view(), name='home'),
path('client_detail/<int:pk>/', ClientDetailView.as_view(),name='client_detail'),
path('credit/<int:pk>/', CreditView, name = 'credit'),
path('debit/<int:pk>/', DebitView, name = 'debit'),
path('create_client/', create_client, name='create_client'),

]
