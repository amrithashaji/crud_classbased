from .models import Contact
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

# listing contacts
class ContactList(ListView): 
    model = Contact

# Details of each contact
class ContactDetail(DetailView): 
    model = Contact

# create new contact
class ContactCreate(CreateView): 
    model = Contact
    fields = ('id', 'name','email','address','phone')
    success_url = "/contacts/"

# update contact
class ContactUpdate(UpdateView): 
    model = Contact
    fields = ('id', 'name','email','address','phone')
    success_url = "/contacts/"

# delete contact
class ContactDelete(DeleteView): 
    model = Contact
    success_url = "/contacts/"



