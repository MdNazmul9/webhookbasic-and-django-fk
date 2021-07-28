from django.urls import path
from .views import PayloadView, ProcessWebhookView

app_name = 'webhook'

urlpatterns = [
    path('payload/',PayloadView.as_view(), name='payload'),   
    path('testpayload/',ProcessWebhookView.as_view(), name='payload'),   
]