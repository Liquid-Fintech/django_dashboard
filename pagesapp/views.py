from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import TicketForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import ResponseModel


def home_page(request):
    return render(request, 'home.html',)


class CreateTicketView(View, LoginRequiredMixin):
    def get(self,request):
        form = TicketForm()
        return render(request, 'create_ticket.html', {'form': form})

    def post(self,request):
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')


class ResponseView(View, LoginRequiredMixin):
    def get(self, request):
        data = ResponseModel.objects.all()
        return render(request, 'response.html', context={'data': data})


# def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)
#             ticket.user = request.user  # If you want to associate tickets with users
#             ticket.save()
#             return redirect('ticket_list')
#     else:
#     form = TicketForm()
#     return render(request, 'tickets/create_ticket.html', {'form': form})