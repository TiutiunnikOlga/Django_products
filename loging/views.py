import secrets

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from loging.forms import LoginRegisterForm
from loging.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = LoginRegisterForm
    success_url = reverse_lazy('loging:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/loging/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Спасибо за регистрацию! Для подтверждения почты, перейди по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(self, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('loging:login'))
