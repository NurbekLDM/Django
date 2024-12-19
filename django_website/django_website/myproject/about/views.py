from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Employee , Company , Contact


def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def company(request):
    company = Company.objects.all()
    return render(request, 'company.html', {'company': company})


from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
