from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import PhoneBookEntry

def godelete(request):
    entries = PhoneBookEntry.objects.all()
    return render(request, 'delete.html', {'entries': entries})

def gosearch(request):
    entries = PhoneBookEntry.objects.all()
    return render(request, 'search.html', {'entries': entries})

def goadd(request):
    entries = PhoneBookEntry.objects.all()
    return render(request, 'add.html', {'entries': entries})

def phonebook_list(request):
    entries = PhoneBookEntry.objects.all()
    return render(request, 'phonebook_list.html', {'entries': entries})

def add_entry(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        if(name!='' and phone_number!=''):
            entry = PhoneBookEntry(name=name, phone_number=phone_number)
            entry.save()
        else:
            return redirect('goadd')    
        return redirect('phonebook_list')

def search_entry(request):
    if request.method == 'POST':
        name = request.POST['search_name']
        try:
            entry = PhoneBookEntry.objects.get(name=name)
            return HttpResponse(f"Phone number for {entry.name}: {entry.phone_number}")
        except PhoneBookEntry.DoesNotExist:
            return HttpResponse(f"No entry found for {name}.")

def delete_entry(request):
    if request.method == 'POST':
        name = request.POST['delete_name']
        try:
            entry = PhoneBookEntry.objects.get(name=name)
            entry.delete()
        except PhoneBookEntry.DoesNotExist:
            pass
    return redirect('phonebook_list')
