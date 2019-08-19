from django.urls import path
from .views import SubscriberCreateView, SubscriberCreateSuccessView

app_name = 'subscribers'

urlpatterns = [
    path('', SubscriberCreateView.as_view(), name='signup'),
    path('thanks/', SubscriberCreateSuccessView.as_view(), name='signup-success'),
]
