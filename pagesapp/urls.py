from django.urls import path
from .views import home_page, CreateTicketView, ResponseView

urlpatterns = [
    path('', home_page, name='home'),
    path('create_ticket/', CreateTicketView.as_view(), name='create_ticket'),
    path('response/', ResponseView.as_view(), name='response')

]
