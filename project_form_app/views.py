from django.shortcuts import render
from . forms import ContactForm  # Update the import statement

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('userName', 'Default Name')
        email = request.POST.get('email', 'default@example.com')
        return render(request, 'form.html', {'name': name, 'email': email})
    else:
        # Handle the case where no POST data is received
        name = "Default Name"
        email = "default@example.com"

    return render(request, 'form.html', {'name': name, 'email': email})

def django_form(request):
  if request.method == 'POST':
     form = ContactForm(request.POST,request.FILES)
     if form.is_valid():
      print(form.cleaned_data)
      return render(request, 'django_form.html', {'form': form})
  else:
     form = ContactForm()
     return render(request, 'django_form.html', {'form': form})