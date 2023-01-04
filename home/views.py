import base64
import datetime
import hashlib
import hmac
import json
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from django.core import serializers
from django.contrib.auth.models import User



from . import forms, models, serializers

def signup_view(request):
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = forms.SignUpForm(request.POST)
    return render(request, 'account/signup.html', {'form': form})


def home(request):
    rides = models.Ride.objects.all()
    return render(
        request=request,
        template_name='home/home.html',
        context={'rides':rides}
    )

def booking(request):
    return render(
        request=request,
        template_name='home/home.html',
        context={}
    )    

def policy(request):

    policy_rules = models.Policy.objects.all()

    return render(
        request=request,
        template_name='home/policy.html',
        context={'rules': policy_rules}
    )    
def faqs(request):
    faqs = models.Faq.objects.all()
    return render(
        request=request,
        template_name='home/faqs.html',
        context={'faqs':faqs}
    )    
def profile(request):
    past_trips = models.Trip.objects.filter(user=request.user).filter(start_time__lte=datetime.datetime.now())
    upcomming_trips = models.Trip.objects.filter(user=request.user).filter(start_time__gte=datetime.datetime.now())
    return render(
        request=request,
        template_name='home/profile.html',
        context={'past_trips':past_trips, 'upcomming_trips':upcomming_trips}
    )    

def setting(request):

    if request.method == 'POST':
        user_form = forms.UserModelForm(data=request.POST, files=request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = forms.UserModelForm(instance=request.user)


    return render(
        request=request, 
        template_name='home/setting.html', 
        context={'user_form':user_form}
        )

def contact_us(request):

    form = forms.CustomerMessageForm()
    context = {'form': form}

    if request.method == 'POST':
        form = forms.CustomerMessageForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            messages.success(request, "Sent Successfully !.")
            form = forms.CustomerMessageForm()
            context = {'form': form}


            subject = 'New Customer Message'
            html_content = f"""
            <span><strong>Name</strong></span>:  <span>{request.POST['full_name']}</span>
            <br>
            <span><strong>Email</strong></span>: <span>{request.POST['email']}</span>
            <br>
            <span><strong>Message</strong></span>: <span>{request.POST['message']}</span>
            <br>
            """
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]

            msg = EmailMessage(subject, html_content, from_email, to_list)
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            print('mail sent')


    return render(
        request=request,
        template_name='home/contact_us.html',
        context=context
    )


def customer_messages(request):
    result = models.CustomerMessage.objects.filter(closed=False)
    serialized_customer_messages = [serializers.CustomerMessageSerializer(instance=i).data for i in (x for x in result)]

    return JsonResponse({'messages':serialized_customer_messages})

@ csrf_exempt
def close_customer_message(request):
    try:
        post_data = json.loads(request.body.decode("utf-8"))
        message_id = post_data['message_id']
        message = models.CustomerMessage.objects.get(id=message_id)
        message.closed = True
        message.save()
        return JsonResponse({'result':True})
    except:
        return JsonResponse({'result':False})
