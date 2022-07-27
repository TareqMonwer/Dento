from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def contact_success_message(request, name):
    ctx = {
        'name': name,
        'message_ok': f'Hey {name}! I\'ll follow-up your mail ASAP,  thanks'
    }
    return render(request, 'contact.html', ctx)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')
        # Send mail
        send_mail(
            f'{name} from Dento', #subject
            message, #message
            email, #from
            ['useurmail@urmail.urext', ], #to
            fail_silently=False,
        )

        return redirect(reverse('contact_success_message', kwargs={'name': name}) + '#contact-form-message')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'service.html')
