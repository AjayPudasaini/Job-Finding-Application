from django.urls import path
from contact import views

urlpatterns = [
    path('contact/us', views.ContactCreateView, name='contact')
]
