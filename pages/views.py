from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ctx = {
            'name': name,
        }
        return render(request, 'contact.html', ctx)
    return render(request, 'contact.html')