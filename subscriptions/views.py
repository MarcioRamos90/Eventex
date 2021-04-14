from django.shortcuts import render
from subscriptions.form import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscrition/subscription_form.html', context)