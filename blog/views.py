from django.views.generic import CreateView, ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.db import transaction

from blog.models import Blog


class BlogView(ListView):
    model = Blog


class CreatePostView(CreateView):
    model = Blog
    fields = ["heading", "content", "photo"]
    template_name = "blog/create_post_view.html"
    success_url = reverse_lazy("blog:create_post")


class BlogListView(ListView):
    model = Blog
    template_name = "blog/page.html"
    context_object_name = "page"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        with transaction.atomic():
            obj = super().get_object(queryset)
            if hasattr(obj, "view_count"):
                obj.view_count += 1
                obj.save(update_fields=["view_count"])

                if obj.view_count == 100:
                    send_mail(
                        "Статья набрала 100 просмотров!",
                        f'Поздравляем! Ваша статья "{obj.heading}" набрала 100 просмотров!',
                        settings.EMAIL_HOST_USER,
                        ["email@email.ru"],
                        fail_silently=False,
                    )
            return obj
