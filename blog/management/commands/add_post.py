from django.core.management.base import BaseCommand
from blog.models import Blog


class Command(BaseCommand):
    help = "Add article to the database"

    def handle(self, *args, **kwargs):
        articles = [
            {"heading": "test", "content": "test content"},
            {"heading": "two", "content": "two content"},
        ]

        for article_data in articles:
            blog, created = Blog.objects.get_or_create(**article_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {blog.heading}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exist: {blog.heading}")
                )
