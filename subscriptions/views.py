from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from subscriptions.form import SubscriptionForm
from subscriptions.models import Subscription

def subscribe(request):
    if request.method == "POST":
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            "subscription/subscription_form.html",
            {"form": form},
        )

    _send_mail(
        "subscription/subscription_email.txt",
        form.cleaned_data,
        "Confirmação de inscrição",
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data["email"],
    )
    
    Subscription.objects.create(**form.cleaned_data)

    messages.success(request, "Inscrição realizada com sucesso!")
    return HttpResponseRedirect("/inscricao/")


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


def new(request):
    return render(
        request, "subscription/subscription_form.html", {"form": SubscriptionForm()}
    )
