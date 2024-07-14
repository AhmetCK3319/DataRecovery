from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Account
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    view_count = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="post_images/")
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        main_category = self.categories.first()
        return reverse("post_detail", args=[main_category.slug, self.slug])


class Comment(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "{} - {}".format(self.post.title, self.author.username)

class SocialModel(models.Model):
    objects = None
    order = models.IntegerField(default=0, verbose_name="sıra", help_text="")
    link = models.URLField(verbose_name="link",help_text="Lütfen doğru url adresi giriniz..",blank=True,default="",)
    icon = models.CharField(max_length=100, verbose_name="ikon", help_text="", blank=True, default="")

    def __str__(self):
        return self.link

    class Meta:
        verbose_name_plural = "Social"
        verbose_name = "Socials"
        ordering = ["order"]



