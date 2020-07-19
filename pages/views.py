from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('message-name')
        email = request.POST.get('message-email')
        message = request.POST.get('message')
        ctx = {
            'name': name,
            'message_ok': f'Hey {name}! I\'ll follow-up your mail ASAP,  thanks'
        }

        # Send mail
        send_mail(
            f'{name} from Dento', #subject
            message, #message
            email, #from
            ['tareqmonwer137@gmail.com', ], #to
            fail_silently=False,
        )

        return render(request, 'contact.html', ctx)
    return render(request, 'contact.html')