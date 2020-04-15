from django.views.generic import TemplateView
from allauth.account.views import SignupView


class HomePage(TemplateView):
    template_name = "base.html"


class SignupView(SignupView):
    template_name = "account/signup.html"
