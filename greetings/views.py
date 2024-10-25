
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Contact

def greetings(request):
    return render(request, 'greetings/greetings.html')

@csrf_exempt  # Remove in production and handle CSRF tokens properly
def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send email notification
        subject = 'New Contact Form Submission'
        body = f'You have received a new message from {name} ({email}):\n\n{message}'
        send_mail(subject, body, email, ['recipient@example.com'])  # Change to your email

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

